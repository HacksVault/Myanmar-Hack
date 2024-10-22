const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const userData = {
    name: null,
    age: null,
    location: null,
    contact_number: null,
    issue: null,
    issue_details: []
};

console.log("Bot: Hello! I'm here to help you. What's your name?");

const askQuestion = (question) => {
    return new Promise((resolve) => {
        rl.question(question, (answer) => {
            resolve(answer);
        });
    });
};

const chatbotConversation = async () => {
    userData.name = await askQuestion("You: ");
    console.log(`Bot: Nice to meet you, ${userData.name}! How old are you?`);
    
    userData.age = await askQuestion("You: ");
    console.log(`Bot: Thank you, ${userData.name}! Where are you located?`);
    
    userData.location = await askQuestion("You: ");
    console.log(`Bot: Got it! What's your contact number?`);
    
    userData.contact_number = await askQuestion("You: ");
    console.log("Bot: Thank you! What issue are you facing? (water, health, food, emergency)");
    
    userData.issue = (await askQuestion("You: ")).toLowerCase();
    
    if (!["water", "health", "food", "emergency"].includes(userData.issue)) {
        console.log("Bot: I'm sorry, I can only help with water, health, food, or emergency issues. Please specify your issue again.");
        return;
    }
    
    console.log(`Bot: Okay, you're facing an issue with ${userData.issue}.`);

    let followUpQuestions;

    switch (userData.issue) {
        case 'water':
            followUpQuestions = [
                "How much water is left for you?",
                "How many people are there?",
                "Please Tell me your need ? "
            ];
            break;
        case 'health':
            followUpQuestions = [
                "How long have you had this problem?",
                "Is anyone nearby for help, and do you have first-aid medication?",
                "What help you want from our side?"
            ];
            break;
        case 'food':
            followUpQuestions = [
                "How much food is left?",
                "How many members are there?",
                "What help you want from our side"
            ];
            break;
        case 'emergency':
            followUpQuestions = [
                "What is your emergency?",
                "Is anyone nearby to help you?",
                "What help you want from our side"
            ];
            break;
    }

    for (const question of followUpQuestions) {
        const answer = await askQuestion(`Bot: ${question} `);
        userData.issue_details.push(answer);
    }

    console.log("\nSummary of the collected information:");
    console.log(`Issue Type: ${userData.issue.charAt(0).toUpperCase() + userData.issue.slice(1)}`);
    console.log(`Name: ${userData.name}`);
    console.log(`Age: ${userData.age}`);
    console.log(`Location: ${userData.location}`);
    console.log(`Contact Number: ${userData.contact_number}`);
    console.log("Issue Details:");
    userData.issue_details.forEach(detail => console.log(`- ${detail}`));

    rl.close();
};

chatbotConversation();
