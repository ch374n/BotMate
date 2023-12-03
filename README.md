Project repository for python based Webex bot for providing TMS & Jenkins alerting, text translation & question answer for pre-configured knowledge base,
based on open-source LLM models.

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

Project Screenshots: 
1. Help menu
   ![image](https://github.com/ch374n/BotMate/assets/39785059/69d2bed9-d031-4ebf-92bf-bb48465f2fe3)
2. TMS Alerting (notifies when tms ticket is assigned to you)
   ![image](https://github.com/ch374n/BotMate/assets/39785059/bea7625d-6699-4ff2-9162-8344c213c8f3)
3. Text translation (from Russian to English)
   ![image](https://github.com/ch374n/BotMate/assets/39785059/9609f81c-5f94-4e43-86e8-3c1b286d6659)
4. Question/Answering based on pre-configured knowledge base
   ![image](https://github.com/ch374n/BotMate/assets/39785059/b6500816-801e-4c47-864d-a06b11540a48)
5. Jenkins Alerting (notifies when configured job fails)
   ![image](https://github.com/ch374n/BotMate/assets/39785059/20f7abc8-8eb3-4924-8951-fda6f61048e8)


Important links: 
1. https://developer.webex.com/docs/api/v1/messages/create-a-message
2. https://adaptivecards.io/explorer/TableCell.html
3. https://developer.webex.com/buttons-and-cards-designer
4. https://0x2142.com/how-to-building-a-basic-webex-chatbot/
5. https://github.com/fbradyirl/webex_bot
