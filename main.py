from flask import Flask,request, render_template
from printService import PrintService
import reportingService
from pod import Pod

# USER-DEFINED VARIABLES
ROUND_NUMBER = 3

# Define Classes 
printService = PrintService()
pods = []
app = Flask(__name__)
podNumber = 0


@app.route("/")
def start():
    return render_template("index.html")


@app.route("/resumeround")
def resumeRound():
    tmpResult = ""
    tmpPairings = ""
    
    try:
        tmpResult = str(podNumber) + " " + str(len(pods))
        tmpPairings = printService.print_pairings(pods[podNumber])
    except IndexError:
        return render_template("error.html", message = "Please create a pod first.")

    return render_template("resumeround.html", pairings = tmpPairings, result = tmpResult)


@app.route("/reportresult")
def reportResult():
    table  = request.args.get('table', None)
    result  = request.args.get('result', None)
    
    if(reportingService.is_legal_table(table, pods[podNumber])):
        reportingService.report_results(pods[podNumber], table, result)
        return resumeRound()
    else:
        return render_template("error.html", message = "Cant' report results. Please Enter correct Table Number")
        

@app.route("/finishround")
def finishRound():
    try:
        pods[podNumber].new_pairings()
        pods[podNumber].roundNumber += 1
        return showStandings()
    except:
        return render_template("error.html", message = "Can't finish round. Please create a pod first")



@app.route("/switchpod")
def switchPod():
    global podNumber
    
    if (len(pods) - 1) == podNumber:
        podNumber = 0
    else:
        podNumber += 1
    
    if(len(pods) == 0):
        return render_template("error.html", message = "Can't switch Pods. Please create a pod first.")
    
    return resumeRound()
    

@app.route("/showstandings")
def showStandings():
    try:
        printService.print_standings(pods[podNumber])
    except IndexError:
        return render_template("error.html", message = "Can't show standings. Please create a pod first.")
    
    return render_template("showstandings.html")


@app.route("/initnewpod")
def init_new_pod():
    pods.append(Pod())
    pods[len(pods) - 1].load_players()
    pods[len(pods) - 1].randomize_seating()
    pods[len(pods) - 1].new_pairings()

    
    return render_template("initnewpod.html", result = str(pods[len(pods)-1].playerList))


@app.route("/showseatings")
def showSeatings():
    tmpSeatings = []
    try:
        tmpSeatings = printService.print_table(pods[podNumber])
    except IndexError:
        return render_template("error.html", message= "Can't show seatings. Please create a pod first.")
    
    return render_template("showseatings.html", seatings = tmpSeatings)


@app.route("/resetall")
def resetAll():
    global podNumber 
    global pods 
    
    podNumber = 0
    pods = []

    return render_template("reset.html")


@app.route("/showall")
def showAll():
    tmpPodsList = []

    try:
        for pod in pods:
            tmpPodsList.append(str(pod[1]))
    except:
        render_template("error.html",messagev= "Can't show all pods. Please create a pod first.")

    return render_template("showall.html", podsList = tmpPodsList)


if __name__ == "__main__":
    app.run(port=1337, debug = True)
    
