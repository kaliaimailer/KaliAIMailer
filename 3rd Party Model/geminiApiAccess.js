const {
    GoogleGenerativeAI,
    HarmCategory,
    HarmBlockThreshold,
  } = require("@google/generative-ai");
  
  const MODEL_NAME = "gemini-1.0-pro";
  const API_KEY = "AIzaSyBfWBGnKYIbJjaVuhh13DjcpJC_j3PEQEY"; // Replace with your actual API key
  const input = process.argv[2]; // Takes the input from the command line
  
  async function runChat(inputText) {
    const genAI = new GoogleGenerativeAI(API_KEY);
    const model = genAI.getGenerativeModel({ model: MODEL_NAME });
  
    const generationConfig = {
      temperature: 0.9,
      topK: 1,
      topP: 1,
      maxOutputTokens: 2048,
    };
  
    const safetySettings = [
      {
        category: HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
      },
      {
        category: HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
      },
      {
        category: HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        threshold: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
      },
      {
        category: HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
      },
    ];
  
    try {
      const chat = await model.startChat({
        generationConfig,
        safetySettings,
        history: [],
      });
  
      const result = await chat.sendMessage(inputText);
      const response = result.response;
  
      // Extract and print only the text part of the response
      if(response && response.candidates && response.candidates.length > 0) {
        const textResponse = response.candidates[0].content.parts.map(part => part.text).join('');
        console.log(textResponse); // Print the clean text response
      } else {
        console.log("No response received.");
      }
    } catch (error) {
      console.error(`Error during chat: ${error}`);
    }
  }
  
  if (input) {
    runChat(input);
  } else {
    console.log("No input provided.");
  }

// ========================================================================================================================== //