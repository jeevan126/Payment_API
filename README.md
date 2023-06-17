# Payment_System

Payment_System is a simple API-based web application to manage coins or balances using the wallet. It contains two APIs namely start-timer and stop_timer. On calling start-timer, the timer will start and 10 coins will be deducted from the wallet for every 1 minute. On calling stop-timer, the timer will stop and give the remaining balance or coins as a response after deduction. We cannot call the stop-timer before the start-timer. In case you call stop-timer before start-time it will redirect to start-timer. Initially, the default balance for the wallet is assumed as 1000 coins.

# Instructions to run the application

1. Download or Clone the repository on your local machine.
2. Create a virtual env and activate it.
3. Install the required modules using pip install requirements.txt command.
4. Run the server using the command - python manage.py runserver.
5. In browser open - http://127.0.0.1:8000/ - It will display the current balance in the wallet.
6. To start timer - http://127.0.0.1:8000/start-timer/
7. To stop timer - http://127.0.0.1:8000/stop-timer/

