# services/prompt_engineering.py
import logging
from services.career_flow import (
    handle_career_interests,
    handle_college_planning1,
    handle_college_planning2,
    handle_college_planning3,
    handle_college_planning4,
    handle_scholarship1,
    handle_biology_interest,
    handle_doctor_interest,
    handle_schorloship2,
    handle_roadmap1,
    handle_roadmap2
)

# def construct_prompt(user_data, user_input):
#     user_input = user_input.lower()

#     # Log the processed input
#     logging.info(f"Processed user input: {user_input}")

#     # Initial greeting or when Alejandra says "hi"
#     if not user_input or user_input == 'hi':
#         logging.info("Initial greeting detected")
#         return [
#             {"role": "system", "content": "You are an AI assistant for Alejandra, a 17-year-old high school student"},
#             {"role": "assistant", "content": "Hi Alejandra, how can I help you today? (Options: 'Career Interests', 'College Applications', 'Goals and Ambitions')"}
#         ]
    
#     # Handling Career Interests Flow
#     if "career" in user_input:
#         return handle_career_interests()
    
#     if "biology" in user_input:
#         return handle_biology_interest()
    
#     if "doctor" in user_input:
#         return handle_doctor_interest()
    
#     if "club" in user_input:
#         return handle_college_planning1()
    
#     if "yale" in user_input:
#         return handle_college_planning2()
#     if "heard" in user_input:
#         return handle_college_planning3()

#     if "neighborhood" in user_input:
#         return handle_college_planning4()
    
#     if "financial" in user_input:
#         return handle_scholarship1()
    
#     if "scholarships" in user_input:
#         return handle_schorloship2()
    
#     if "CUNY" in user_input:
#         return handle_roadmap1()
    
#     if "roadmap" in user_input:
#         return handle_roadmap2()
    



#     # Default or fallback response
#     return [
#         {"role": "system", "content": user_data},
#         {"role": "user", "content": user_input}
#     ]

def construct_prompt(user_data, user_input):
    user_input = user_input.lower()

    # Log the processed input
    logging.info(f"Processed user input: {user_input}")

    # Initial greeting or when Alejandra says "hi"
    if not user_input or user_input == 'hi':
        logging.info("Initial greeting detected")
        return [
            {"role": "system", "content": "You are an AI assistant for Alejandra, a 17-year-old high school student"},
            {"role": "assistant", "content": "Hi Alejandra, how can I help you today? (Options: 'Career Interests', 'College Applications', 'Goals and Ambitions')"}
        ]

    # Keyword-based handling, irrespective of flow
    keyword_mappings = {
        "career": handle_career_interests,
        "biology": handle_biology_interest,
        "doctor": handle_doctor_interest,
        "club": handle_college_planning1,
        "yale": handle_college_planning2,
        "heard": handle_college_planning3,
        "neighborhood": handle_college_planning4,
        "financial": handle_scholarship1,
        "scholarships": handle_schorloship2,
        "cuny": handle_roadmap1,
        "roadmap": handle_roadmap2
    }

    # Check for keywords in user input and return corresponding response
    for keyword, handler in keyword_mappings.items():
        if keyword in user_input:
            logging.info(f"Keyword '{keyword}' detected, triggering corresponding handler.")
            return handler()

    # Default or fallback response if no keyword matches
    logging.info("No specific keyword detected, using fallback response.")
    return [
        {"role": "system", "content": user_data},
        {"role": "user", "content": user_input},
        {"role": "assistant", "content": "I’m not sure how to help with that. Could you please clarify or try asking something else related to 'Career Interests', 'College Applications', or 'Goals'?"}
    ]
