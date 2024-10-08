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
    return [
        # Makes sense. A lot of colleges have pre-med. Can I provide some additional options for you to consider? I’ll share the different admissions requirements and typical student profile of an admitted student so you can see what the different colleges are looking for Would you like help with that?"
        {"role": "system", "content": "you are a friendly ai find out if she would like help with additional options for colleges with pre-med programs.without re-greeting her"},
        {"role": "assistant", "content": "Makes sense. A lot of colleges have pre-med. Can I provide some additional options for you to consider? I’ll share the different admissions requirements and typical student profile of an admitted student so you can see what the different colleges are looking for Would you like help with that?"}
    ]

def handle_scholarship1():
    # AI: "That’s perfectly fine! There are many scholarships available for students pursuing health sciences. I can help you search for scholarships and guide you through the application process. Would that be helpful?"

    return [
        {"role": "system", "content": "you are a friendly ai find out if she would like help with searching for scholarships and guidance through the application process.without re-greeting her"},
        {"role": "assistant", "content": "That’s perfectly fine! There are many scholarships available for students pursuing health sciences. I can help you search for scholarships and guide you through the application process. Would that be helpful?"}
    ]

def handle_schorloship2():
    # Can't have this -- she;s undocumented, so she's not eligible -- her options are CUNY or SUNY because private universities are out of reach for her due to finances

    return [
        {"role": "system", "content": "you are a friendly ai shes undocumented and private universities are out of reach for her due to finances ask her if she has considered applying to cuny or suny schools.without re-greeting her"},
        {"role": "assistant", "content": "I understand that you are undocumented and private universities are out of reach for you due to finances. Have you considered applying to CUNY or SUNY schools?"}
        ]

def handle_roadmap1():
    # AI: "Now that you have a list of colleges you’re interested in, I’ll help you create a roadmap to get your profile to reflect more like the ones of the typically admitted candidates at these schools. We’ll focus on your high school courses, preparing for college applications, and finding internships, volunteering or other experiences that will help your profile stand out. Does that sound good?"

    return [
        {"role": "system", "content": "you are a friendly ai find out if she would like help creating a roadmap to get her profile to reflect more like the ones of the typically admitted candidates at the schools she is interested in.without re-greeting her"},
        {"role": "assistant", "content": "Now that you have a list of colleges you’re interested in, I’ll help you create a roadmap to get your profile to reflect more like the ones of the typically admitted candidates at these schools. We’ll focus on your high school courses, preparing for college applications, and finding internships, volunteering or other experiences that will help your profile stand out. Does that sound good?"}
    ]

def handle_roadmap2():
    # Return the roadmap tasks in a structured format
    return [
        {"role": "system", "content": "You are a friendly AI helping Alejandra build a roadmap to improve her profile for Pre-med applications.without re-greeting her."},
        {"role": "assistant", "content": 
            "Great! I’ll include tasks like preparing for the SAT, finding internships, and applying for scholarships to keep you organized and ready for each step. Here's a personalized roadmap for you:"},

        # Phase 1: High School Senior Year
        {"role": "assistant", "content": 
            "Phase 1: High School Senior Year\n"
            "- Continue excelling in Biology, Chemistry, and Math.\n"
            "- Take AP courses if available, particularly in Biology and Chemistry.\n"
            "- SAT/ACT Prep: Schedule study sessions and aim for scores that align with Pre-med admission requirements.\n"
            "- Target GPA: Keep GPA above 3.5."},

        # Extracurricular Activities
        {"role": "assistant", "content": 
            "Extracurricular Activities:\n"
            "- Join the Science Club and participate in health sciences-related projects.\n"
            "- Volunteer at local hospitals or clinics.\n"
            "- Explore summer internships in health organizations."},

        # College Planning
        {"role": "assistant", "content": 
            "College Planning:\n"
            "- Research Pre-med programs at CUNY, SUNY, and other regional schools in NYC.\n"
            "- Schedule college visits or virtual tours to get insight into campus life.\n"
            "- Research backup schools with strong Pre-med programs and apply to them as well."},

        # College Applications
        {"role": "assistant", "content": 
            "Start College Applications:\n"
            "- Begin working on your Common App or Coalition App. Focus on essays that highlight your passion for biology and health sciences.\n"
            "- Approach teachers for letters of recommendation."},

        # Phase 2: Scholarships and Financial Aid
        {"role": "assistant", "content": 
            "Phase 2: Scholarships and Financial Aid:\n"
            "- Research scholarships for health sciences, gather documents like personal statements and letters of recommendation.\n"
            "- Explore FAFSA eligibility and apply for local grants for students pursuing health sciences."},

        # Phase 3: Finalizing College Applications
        {"role": "assistant", "content": 
            "Phase 3: Finalizing College Applications:\n"
            "- Review all applications and submit by December for regular decision deadlines.\n"
            "- Ensure all scholarship applications are submitted on time.\n"
            "- Follow up with colleges to track submission statuses."},

        # Phase 4: Summer Before College
        {"role": "assistant", "content": 
            "Phase 4: Summer Before College:\n"
            "- Participate in internships or volunteer at hospitals, research labs, or health organizations.\n"
            "- Prepare for college by taking online courses or shadowing healthcare professionals.\n"
            "- Register for college orientation programs to meet advisors and get acclimated."},

        {"role": "assistant", "content": 
            "I’ve created your personalized roadmap, Alejandra. You’re well on your way of pursuing pre-med! Keep me updated as you complete activities, and I’ll help with your next steps. We can check in every few weeks to track your progress."}
    ]

