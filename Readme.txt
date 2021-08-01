This is a prototype chatbot for banking assistance that I created using Rasa. The software is divided into three portions:
1. Under "bank" folder, there is a django webapp that creates a dummy bank database from which the chatbot can retrieve various banking information to provide to the user for request.
2. Under "rasa_chatbot" folder, there is the chatbot code developed using the Rasa framework.
3. Under "rasa_widget" folder, there are html and javascript files which creates a GUI web platform for the user to interact with the chatbot.

How to run:
1. Install Python 3.6.8.
2. Install Rasa 2.0 and Tensorflow 2.0.
3. Run the django application under "bank" folder.
4. Open command prompt in "rasa_chatbot" folder and type "rasa run".
5. Open the "index.html" file in "rasa_widget" folder to start the webapp and communicate with the chatbot.


For further inquiry, please email me at "msaquibhasan@gmail.com".