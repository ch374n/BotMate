Project repository for python based Webex bot

Software Requirement: 
1. Maven
2. Python 3.11
3. npm (for running docs on local)

How to run locally ? 
```
Step 1: Clone this repo

Step 2: Rename example.env in chatbot-impl/example.env to .env and replace corresponding 
API keys

Step 3: Navigate to chatbot-impl and install all dependencies using pip install .

Step 4: If you're running this project using maven, then include python path in <executable> 
tag of pom.xml  

Step 5: From maven plugins section run exec goal OR you can simply run python main.py


```

How to run docs locally ? 
```

Step 1: go inside botmate-docs and execute npm install
Step 2: execute npm run start command and visit localhost:3000

```

Important links: 
1. https://developer.webex.com/docs/api/v1/messages/create-a-message
2. https://adaptivecards.io/explorer/TableCell.html
3. https://developer.webex.com/buttons-and-cards-designer
4. https://0x2142.com/how-to-building-a-basic-webex-chatbot/
5. https://github.com/fbradyirl/webex_bot
