# TODO
* Feature: event saving and loading functionality
* Feature: Main -> Reporting: Check if all Results entered before finish Round
  

* Bug: printService -> printTable: Odd amount of Players lead to an issue at the table (double/missing players)
* Bug: Switching between Pods during running Tournament shifts existing results to wrong table

# DONE
* Implemented multi-draft pod infrastructure by using independent larger tracking pods that shadow pairings and results.
* Refactored reporting features to reportingService
* Refactored and split up code to allow for integration down the line
* cleaned up and added some ASCII formatting to the CLI
* results reporting
* input validation for results reporting
* shuffle groups for seatings generation

# ROADMAP
* proper error handling
* DB and stats integration (hosting)
* GUI