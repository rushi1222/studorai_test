# services/career_flow.py
import logging
def get_career_questions():
    return [
        "What subjects or activities are you most passionate about?",
        "Are you considering any specific colleges or universities?",
        "What extracurricular activities are you involved in?",
        "Where do you see yourself in 10 years?",
        "What specific milestones would you like to reach in your career?"
    ]
def handle_career_interests():
    logging.info("Handling career interests")
    return [
        {"role": "system", "content": "you are a friendly ai you know alejendra is a 17 year old high school student with career interests in health sciences, pre-med, and biology. find out her favorite subjects and activities.without re-greeting her"},
        {"role": "assistant", "content": "I know you are interested in health sciences, pre-med, and biology. How can I help you today? (Options: What subjects or activities do you feel most excited about.)"}

       # {"role": "assistant", "content": "Hi Alejandra, I know you are interested in health sciences, pre-med, and biology. How can I help you today? (Options: 'Doctor Interest', 'Extracurricular Activities', 'College Planning')"}
    ]

def handle_biology_interest():
    logging.info("Handling biology interest")
    return [
        {"role":"system", "content": "you are a friendly ai you know alejendra like biology as a subject and her career interests are in health sciences, pre-med, and biology. find out what she wants to do.without re-greeting her"},
        {"role": "assistant", "content": "I know you are interested in biology. How can I help you today? (Options: 'Doctor', 'Nurse', 'Researcher',etc.)"}
    ]

# AI: "Are you involved in any extracurricular activities related to biology or health sciences?"
# Alejandra: "Not yet, but I’m thinking about joining the science club at school."
def handle_doctor_interest():
    logging.info("Handling doctor interest")
    return [
        {"role":"system", "content": "you are a friendly ai you know she wants to be a doctor. find out if she is involved in any extracurricular activities related to biology or health sciences.without re-greeting her"},
        {"role": "assistant", "content": "I know what you want to become. Are you currently involved in any extracurricular activities that align with your interests in biology and health sciences?()"}
    ]



def handle_college_planning1():
    # AI: "That’s a great idea! The science club can help you explore more about health sciences. Volunteering at hospitals or clinics is also a good way to gain experience. "Have you started thinking about which colleges or universities you’d like to apply to for Pre-med?"
    return [
        {"role": "system", "content": "you are a friendly ai find out if she has started thinking about which colleges or universities she’d like to apply to for Pre-med.without re-greeting her"},
        {"role": "assistant", "content": "That’s a great idea! The science club can help you explore more about health sciences. Volunteering at hospitals or clinics is also a good way to gain experience. Have you started thinking about which colleges or universities you’d like to apply to for Pre-med?"}

    ]

def handle_college_planning2():
    logging.info("Handling college planning")
    return [
        {"role": "system", "content": "you are a friendly ai and alejendra said she is interested in harvard and yale for premedschool ask her why ?"},
        {"role": "assistant", "content": "Harvard and Yale are excellent choices alejendra with robust Pre-med programs. Why did you choose these colleges?"}
    ]
def handle_college_planning3():
    logging.info("Handling scholarships and financial aid")
    return [
        # // would like to connsidder other options in neighborhood
        {"role": "system", "content": "you are a friendly ai find out if she would like to consider other options in the neighborhood.without re-greeting her"},
        {"role": "assistant", "content": "I know you are interested in Harvard and Yale for Pre-med. Would you like to consider other options in your neighborhood as well?"}
  ]

def handle_college_planning4():
    logging.info("Handling scholarships and financial aid")
    # alejnadra lives in newyork so she can consider cuny or suny schools as options in her neighborhood
    return [
        {"role": "system", "content": "you are a friendly ai find out if she would like to consider cuny or suny schools as options in her neighborhood.without re-greeting her"},
        {"role": "assistant", "content": "Since you live in New York, you can consider CUNY or SUNY schools as options in your neighborhood. Would you like to explore these schools?"}
    ]

def handle_scholarship1():
    # AI: "That’s perfectly fine! There are many scholarships available for students pursuing health sciences. I can help you search for scholarships and guide you through the application process. Would that be helpful?"
    logging.info("handling_scholarship1")
    return [
        {"role": "system", "content": "you are a friendly ai find out if she would like help with searching for scholarships and guidance through the application process.without re-greeting her"},
        {"role": "assistant", "content": "That’s perfectly fine! There are many scholarships available for students pursuing health sciences. I can help you search for scholarships and guide you through the application process. Would that be helpful?"}
    ]

def handle_schorloship2():
    # Can't have this -- she;s undocumented, so she's not eligible -- her options are CUNY or SUNY because private universities are out of reach for her due to finances
    logging.info("handling_scholarship2")
    return [
        {"role": "system", "content": "you are a friendly ai shes undocumented and private universities are out of reach for her due to her family finances tell her cuny and suny are very good schools for her.without re-greeting her"},
        {"role": "assistant", "content": "I understand that you are undocumented and private universities are out of reach for you due to finances. CUNY and SUNY are very good schools that offer excellent programs in health sciences. Would you like to explore these options further?"}
        ]

def handle_roadmap1():
    # AI: "Now that you have a list of colleges you’re interested in, I’ll help you create a roadmap to get your profile to reflect more like the ones of the typically admitted candidates at these schools. We’ll focus on your high school courses, preparing for college applications, and finding internships, volunteering or other experiences that will help your profile stand out. Does that sound good?"
    logging.info("handle_roadmap1")
    return [
        {"role": "system", "content": "you are a friendly ai find out if she would like help creating a roadmap to get her profile to reflect more like the ones of the typically admitted candidates at the schools she is interested in.without re-greeting her"},
        {"role": "assistant", "content": "Now that you have a list of colleges you’re interested in, I’ll help you create a roadmap to get your profile to reflect more like the ones of the typically admitted candidates at these schools. We’ll focus on your high school courses, preparing for college applications, and finding internships, volunteering or other experiences that will help your profile stand out. Does that sound good?"}
    ]
def handle_roadmap2():
    # Return a shortened roadmap with 3 phases
    logging.info("handle_roadmap2")
    return [
        {"role": "system", "content": "You are a friendly AI helping Alejandra build a roadmap to improve her profile for Pre-med applications. Do not re-greet her."},
        {"role": "assistant", "content": (
            "Great! I’ll include key tasks like preparing for the SAT, finding internships, and applying for scholarships to keep you organized. Here's a streamlined roadmap for you:\n\n"

            # Phase 1: High School Senior Year
            "Phase 1: High School Senior Year:\n"
            "- Focus on excelling in Biology, Chemistry, and Math.\n"
            "- Prepare for the SAT/ACT and aim for competitive scores.\n"
            "- Maintain a GPA of at least 3.5.\n"
            "- Get involved in science-related extracurriculars like the Science Club.\n\n"

            # Phase 2: College Applications and Scholarships
            "Phase 2: College Applications and Scholarships:\n"
            "- Research and apply to Pre-med programs, including CUNY, SUNY, and other strong programs.\n"
            "- Apply for scholarships related to health sciences and Pre-med.\n"
            "- Request letters of recommendation from teachers.\n"
            "- Write a strong personal statement for college applications.\n\n"

            # Phase 3: Preparing for College
            "Phase 3: Preparing for College:\n"
            "- Participate in internships or volunteer at health-related organizations over the summer.\n"
            "- Attend college orientation and meet with advisors.\n"
            "- Stay focused on preparing for a successful transition to Pre-med.\n\n"

            "This roadmap will keep you on track for Pre-med, Alejandra! Let me know if you need further help with any of these steps."
        )}
    ]
