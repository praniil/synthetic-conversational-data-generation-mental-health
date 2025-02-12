import csv
import random

# Define templates for user inputs and chatbot responses
templates = {
    "sleep": [
        ("I’ve been sticking to a bedtime routine, and for the first time in months, I’m sleeping through the night. It feels {emotion}!", 
         "That’s fantastic! A consistent sleep routine can work wonders for your mental and physical health. Keep prioritizing rest—you’re giving your body the care it deserves."),
        ("I stopped using my phone an hour before bed, and I’ve noticed I fall asleep faster and wake up feeling {emotion}.", 
         "That’s a great habit! Reducing screen time before bed can make a huge difference in sleep quality. You’re making such healthy choices for your well-being—keep it up!"),
        ("I started using a sleep meditation app, and it’s helping me relax before bed. I’m actually looking forward to bedtime now!", 
         "That’s wonderful! Sleep meditation can be such a calming ritual. It’s great to hear you’re finding joy in rest—it’s such an important part of self-care."),
        ("I’ve been incorporating relaxation techniques, like deep breathing before bed, and it’s helping me sleep so much better. I feel more {emotion} in the mornings.", 
         "Relaxation techniques are a great way to prepare your body for rest. It’s amazing how they can help reduce stress before sleep. Keep making that time for yourself."),
        ("I’ve been avoiding heavy meals late at night, and it’s helped improve my sleep quality. I wake up feeling more {emotion} and refreshed.", 
         "That’s a smart choice! Avoiding late-night meals can have a significant impact on sleep. You’re taking steps to care for your body—keep it up."),
        ("I’ve been drinking chamomile tea before bed, and it’s helping me wind down and sleep better. I wake up feeling more {emotion}.", 
         "That’s a soothing choice! Herbal teas like chamomile are perfect for relaxing before sleep. You’re doing great in prioritizing your rest."),
        ("I’ve started keeping my room cooler at night, and it’s making a huge difference in my sleep quality. I feel more {emotion} when I wake up.", 
         "A cooler environment can really improve sleep! It’s wonderful to hear how you’re fine-tuning your routine for better rest."),
        ("I’ve been listening to calming music before bed, and it’s helping me drift off so much easier. I wake up feeling more {emotion}.", 
         "Music can be such a powerful tool for relaxation. It’s great to hear how it’s helping you unwind and sleep better. Keep creating that peaceful atmosphere."),
        ("I’ve been trying to wake up at the same time every day, even on weekends, and it’s helping me feel more {emotion} and consistent.", 
         "That’s such a healthy habit! A consistent wake-up time can really regulate your sleep cycle. You’re doing amazing—keep it up!"),
    ],
    "anger": [
        ("I used to snap at people when I was stressed, but now I take a deep breath and pause before reacting. It’s helping me stay {emotion}.", 
         "That’s such a powerful shift! Managing anger with mindfulness is a skill that takes practice, and you’re doing amazing. Keep celebrating these small but meaningful changes."),
        ("I started journaling about my anger triggers, and it’s helping me understand and manage them better. I feel more {emotion} now.", 
         "Journaling is such a powerful way to process emotions. It’s amazing how self-awareness can transform how we handle challenges. You’re doing the work, and it’s paying off!"),
        ("I’ve been channeling my anger into creative projects, like {activity}. It’s helping me express myself in a healthier way.", 
         "That’s such a beautiful way to transform anger into something positive! Creativity can be incredibly therapeutic. You’re turning challenges into opportunities for growth—keep shining!"),
        ("When I feel anger rising, I focus on my breathing to calm down, and it’s making me feel more {emotion} and in control.", 
         "Breathing exercises are a great way to regain calm. You’re learning to manage your emotions in such a healthy way. Keep practicing—you’re doing awesome."),
        ("Instead of lashing out, I’ve been practicing mindfulness, and it’s helping me stay more {emotion} and composed.", 
         "Mindfulness is such a powerful tool! It’s amazing to hear how it’s helping you stay grounded in tough moments. Keep focusing on that inner peace."),
        ("I’ve started counting to ten when I feel myself getting angry, and it’s really helping me regain control and feel {emotion}.", 
         "That’s a great technique! Taking a moment before reacting can make all the difference in staying calm. You’re building emotional resilience—keep it up!"),
        ("I’ve been reminding myself that it’s okay to feel angry, but it’s how I respond that matters. It’s helping me stay {emotion}.", 
         "That’s such a mature perspective! Acknowledging your emotions while choosing how to act is a sign of real growth. You’re doing amazing."),
        ("I’ve been practicing empathy when I feel angry, trying to see things from the other person’s perspective. It’s helping me feel more {emotion}.", 
         "Empathy is such a powerful way to diffuse anger. It’s inspiring to hear how you’re using it to navigate tough situations. Keep practicing—you’re doing great."),
    ],
    "anxiety": [
        ("I’ve been practicing grounding techniques when I feel anxious, and it’s helping me stay present instead of spiraling into worry.", 
         "Grounding techniques are such a helpful tool! It’s inspiring to hear how you’re taking control of your anxiety. Every step forward is a victory—keep going!"),
        ("I’ve been challenging my anxious thoughts by asking myself, ‘Is this true?’ It’s helping me break free from negative cycles.", 
         "That’s such a powerful technique! Questioning your thoughts is a great way to regain control. You’re building mental strength every day—keep trusting yourself."),
        ("I’ve been using a gratitude journal to focus on the good things in my life, and it’s helping me feel less {emotion}.", 
         "Gratitude is such a powerful practice! It’s wonderful to hear how it’s helping you shift your perspective. You’re finding light even in tough moments—keep shining!"),
        ("I’ve started using mindful breathing exercises when I feel anxious, and it’s making a big difference in how I handle stress.", 
         "Mindful breathing can help reset your body and mind in moments of stress. It’s amazing to hear how it’s helping you stay balanced. Keep breathing—you’re doing great."),
        ("I’ve been spending a few minutes each day doing mindfulness meditation to calm my nerves, and it’s helping me feel more {emotion}.", 
         "Meditation is such a great practice for reducing anxiety. It’s inspiring to hear how it’s making a difference in your life. Keep making that time for yourself."),
        ("I’ve been visualizing peaceful scenes to calm myself when I feel anxious, and it’s helping me feel more {emotion}.", 
         "Visualization is such a powerful tool to reduce anxiety! It’s wonderful to hear how it’s giving you peace. Keep using that method—it’s making a difference."),
        ("I’ve been reminding myself that anxiety doesn’t define me, and it’s helping me feel more {emotion}.", 
         "That’s such a powerful mindset! Separating yourself from your anxiety is a huge step. You’re doing amazing—keep reminding yourself of your strength."),
        ("I’ve been talking to a friend when I feel anxious, and it’s helping me feel less alone and more {emotion}.", 
         "Connection is so healing. It’s wonderful to hear how you’re reaching out for support. Keep nurturing those relationships—you’re not alone in this."),
    ],
    "depression": [
        ("I’ve been reaching out to friends more often, and it’s helping me feel less {emotion}. It’s like a weight is lifting off my shoulders.", 
         "Connection is so healing. It takes courage to reach out, and I’m so proud of you for taking that step. Keep nurturing those relationships—you’re not alone in this journey."),
        ("I’ve been setting small, achievable goals for myself, like {activity}. It’s helping me feel more {emotion}.", 
         "Small goals can lead to big changes! It’s inspiring to hear how you’re taking steps to care for yourself. Every little effort counts—you’re doing amazing."),
        ("I’ve been practicing self-compassion when I feel angry at myself. It’s helping me let go of guilt and move forward.", 
         "Self-compassion is such a powerful tool! It’s amazing to hear how you’re treating yourself with kindness. You’re growing every day—keep embracing that love for yourself."),
        ("I’ve been finding comfort in my hobbies again, like {activity}, and it’s helping me feel more {emotion}.", 
         "Engaging in hobbies is such a great way to bring joy back into your life. It’s wonderful to hear that you’re reconnecting with things that bring you peace."),
        ("I’ve been focusing on making small changes to my routine, and it’s been helping me feel more {emotion}.", 
         "Small changes can make a big difference in how we feel. It’s so encouraging to hear that you’re taking charge of your day—keep it up."),
        ("I’ve been trying new relaxation techniques, like {activity}, and it’s helping me feel more {emotion}.", 
         "Exploring new methods of self-care is such a positive step! It’s great to hear that you’re finding new ways to relax. Keep trying new things—you’re doing wonderful."),
        ("I’ve been spending more time in nature, and it’s helping me feel more {emotion} and connected to the world.", 
         "Nature has such a calming effect. It’s wonderful to hear how it’s helping you feel grounded and at peace. Keep finding those moments outdoors."),
        ("I’ve been reminding myself that progress isn’t linear, and it’s okay to have tough days. It’s helping me feel more {emotion}.", 
         "That’s such a healthy perspective! Accepting the ups and downs is a sign of real growth. You’re doing amazing—keep being kind to yourself."),
    ],
    "gratitude": [
        ("I started a gratitude journal, and it’s helping me focus on the positive things in my life. I feel more {emotion} and less stressed.", 
         "Gratitude is such a transformative practice! It’s wonderful to hear how it’s shifting your perspective. Keep focusing on the good—it’s making a difference."),
        ("I’ve been taking a moment each day to appreciate the small things, like {activity}. It’s making me feel more {emotion}.", 
         "That’s such a beautiful habit! Finding joy in the little things can bring so much peace. You’re cultivating a mindset of abundance—keep it up!"),
        ("I’ve been telling the people I care about how grateful I am for them, and it’s making me feel more {emotion}.", 
         "Expressing gratitude to others can strengthen relationships and uplift both of you. It’s wonderful to hear how you’re nurturing your connections."),
        ("Every morning, I list three things I’m grateful for, and it helps set a positive tone for the day. I feel more {emotion} because of it.", 
         "Starting your day with gratitude is a beautiful practice. It’s great to hear how it’s setting a positive foundation for the rest of your day. Keep embracing that energy."),
        ("I’ve been making a habit of pausing to appreciate nature, and it’s helping me feel more {emotion}.", 
         "Nature can be so calming and grounding. It’s inspiring to hear how it’s helping you stay present and peaceful. Keep finding moments to connect with the world around you."),
        ("I’ve started expressing gratitude for my body, and it’s helping me feel more {emotion} and connected to myself.", 
         "That’s such a powerful practice! Appreciating your body can bring a deep sense of love and care. Keep embracing that gratitude—you’re doing amazing."),
        ("I’ve been reflecting on the lessons I’ve learned from tough times, and it’s helping me feel more {emotion}.", 
         "That’s such a mature perspective! Finding meaning in challenges is a sign of real growth. You’re doing amazing—keep reflecting and growing."),
        ("I’ve been practicing gratitude for the people who support me, and it’s helping me feel more {emotion}.", 
         "Acknowledging your support system is such a beautiful practice. It’s wonderful to hear how it’s helping you feel connected and loved. Keep nurturing those relationships."),
    ],
    "self-care": [
        ("I’ve been taking time each day to do something just for me, like {activity}. It’s helping me feel more {emotion} and less overwhelmed.", 
         "Self-care is so important! It’s inspiring to hear how you’re prioritizing your well-being. Keep making time for yourself—you deserve it."),
        ("I started saying ‘no’ to things that drain my energy, and it’s helping me feel more {emotion}.", 
         "Setting boundaries is a powerful act of self-care! It’s amazing to hear how you’re protecting your energy. Keep honoring your needs—you’re doing great."),
        ("I’ve been dedicating Sundays to rest and relaxation, and it’s helping me feel more {emotion} and recharged for the week ahead.", 
         "That’s such a great practice! Taking a dedicated day for self-care is a wonderful way to reset. Keep enjoying those moments of rest—you’re doing awesome."),
        ("I’ve been investing in my physical health by going for walks, and it’s helping me feel more {emotion}.", 
         "Walking is such a great way to boost your mood and physical health. It’s amazing that you’re prioritizing your body’s needs—keep moving, you’re doing great."),
        ("I’ve been practicing deep breathing exercises throughout the day to stay calm, and it’s helping me feel more {emotion}.", 
         "Breathing exercises are such a wonderful way to reduce stress. It’s inspiring to hear how you’re making them part of your routine—keep it up!"),
        ("I’ve been treating myself to small indulgences, like {activity}, and it’s helping me feel more {emotion}.", 
         "It’s so important to treat yourself with kindness. It’s wonderful to hear how you’re finding joy in the little things. Keep celebrating yourself—you deserve it."),
        ("I’ve been focusing on getting enough sleep, and it’s helping me feel more {emotion} and energized.", 
         "Sleep is such a key part of self-care. It’s great to hear how you’re prioritizing rest. Keep making that time for yourself—you’re doing amazing."),
        ("I’ve been spending time doing things I love, like {activity}, and it’s helping me feel more {emotion}.", 
         "Doing things you love is such a great way to recharge. It’s wonderful to hear how you’re making time for joy. Keep nurturing that happiness—you’re doing great."),
    ],
    "therapy progress": [
        ("My therapist helped me reframe a negative thought today. It’s like a lightbulb went off—I finally feel {emotion}.", 
         "That ‘lightbulb’ moment is such a beautiful sign of progress. Hope is a foundation for healing. Keep trusting the process—you’re doing the work, and it shows."),
        ("I’ve been applying the coping strategies I learned in therapy, and they’re really helping me manage my emotions better.", 
         "That’s incredible progress! It’s amazing to hear how you’re putting what you’ve learned into practice. Keep building those skills—you’re doing amazing."),
        ("I’ve been exploring new therapeutic techniques, and I’m starting to feel more {emotion}.", 
         "It’s so exciting to hear that you’re embracing new techniques! Therapy is such a personal journey, and it’s great to hear that you’re making strides."),
        ("I’ve been opening up more in therapy, and it’s helping me feel more {emotion} and understood.", 
         "That’s such a brave step! Opening up can be challenging, but it’s so rewarding. Keep being honest with yourself—you’re doing amazing."),
        ("I’ve been setting goals with my therapist, and it’s helping me feel more {emotion} and focused.", 
         "Goal-setting is such a great way to stay motivated. It’s inspiring to hear how you’re working towards your growth. Keep going—you’re doing great."),
        ("I’ve been reflecting on my progress in therapy, and it’s helping me feel more {emotion} and hopeful.", 
         "Reflecting on your progress is such a powerful practice. It’s wonderful to hear how it’s giving you hope. Keep celebrating your growth—you’re doing amazing."),
    ],
        "social connections": [
        ("I reached out to a friend today and had a really meaningful conversation. It reminded me that I’m not alone in this.", 
         "Connection is so healing. It’s wonderful to hear how you’re nurturing your relationships. Keep reaching out—you’re building a strong support system."),
        ("I joined a new group activity, and it’s helping me feel more {emotion}. I’m starting to feel like I belong.", 
         "That’s such a brave step! Building new connections can be so rewarding. Keep putting yourself out there—you’re doing great."),
        ("I’ve been making more time for family, and it’s helping me feel more {emotion} and connected.", 
         "Spending time with loved ones is such a wonderful way to feel grounded. It’s great to hear how you’re prioritizing those relationships."),
    ],
    "mindfulness": [
        ("I’ve been practicing mindfulness meditation, and it’s helping me stay present and calm throughout the day.", 
         "Mindfulness is such a powerful tool! It’s inspiring to hear how it’s helping you stay grounded. Keep practicing—you’re building a strong foundation for peace."),
        ("I’ve been focusing on my breath whenever I feel stressed, and it’s helping me stay {emotion}.", 
         "That’s such a helpful technique! It’s amazing to hear how you’re using mindfulness to manage stress. Keep breathing—you’re doing great."),
        ("I’ve been bringing mindfulness into everyday tasks, like {activity}, and it’s helping me feel more {emotion}.", 
         "Incorporating mindfulness into daily activities can bring such a sense of peace. It’s wonderful to hear how you’re staying present in all parts of your day."),
    ],
    "exercise": [
        ("I started going for daily walks, and it’s helping me clear my mind and feel more {emotion}.", 
         "Exercise is such a great way to boost your mood and energy! It’s inspiring to hear how you’re taking care of your body and mind. Keep moving—you’re doing amazing."),
        ("I’ve been doing yoga regularly, and it’s helping me feel more {emotion}.", 
         "Yoga is such a wonderful practice for both the body and mind! It’s great to hear how it’s helping you feel better. Keep flowing—you’re doing great."),
        ("I’ve been doing strength training, and it’s helping me feel more {emotion} and empowered.", 
         "Strength training is such a great way to build both physical and mental strength. It’s fantastic to hear how it’s making a difference in your life."),
    ],
    "nutrition": [
        ("I’ve been eating more whole foods, and I can feel the difference in my energy levels and mood.", 
         "Nutrition is so important for mental health! It’s inspiring to hear how you’re fueling your body with care. Keep nourishing yourself—you’re doing amazing."),
        ("I started drinking more water throughout the day, and it’s helping me feel more {emotion}.", 
         "Hydration is key to feeling your best! It’s great to hear how you’re taking care of yourself. Keep sipping—you’re doing great."),
        ("I’ve been experimenting with new healthy recipes, and it’s making me feel more {emotion}.", 
         "Trying new recipes can be so fun and nourishing! It’s awesome to hear how you’re making healthy choices for yourself."),
    ],
    "personal growth": [
        ("I’ve been reading self-help books, and they’re giving me new tools to navigate my emotions and relationships.", 
         "That’s such a proactive step! It’s inspiring to hear how you’re investing in your growth. Keep learning—you’re doing amazing."),
        ("I’ve been reflecting on my values and setting intentions for the future. It’s helping me feel more {emotion}.", 
         "That’s such a powerful practice! It’s amazing to hear how you’re creating a life that feels meaningful to you. Keep dreaming—you’re doing great."),
        ("I’ve been setting long-term goals, and it’s helping me feel more {emotion} and focused.", 
         "Goal-setting is such a great way to stay motivated and intentional. It’s inspiring to hear how you’re planning for your future."),
    ]
}

emotions = [
    "calm", "hopeful", "energized", "peaceful", "content", "balanced", "focused", "joyful", 
    "relieved", "motivated", "grateful", "excited", "empowered", "optimistic", "serene", 
    "stressed", "overwhelmed", "anxious", "fearful", "angry", "frustrated", "confused", "guilty", 
    "ashamed", "sad", "lonely", "hopeless", "blissful", "thankful", "inspired", "nervous", 
    "confident", "defeated", "hopeful", "euphoric", "indifferent", "despondent", "relaxed", 
    "insecure", "enthusiastic", "fearless", "mournful", "grief-stricken", "contented", 
    "embarrassed", "disappointed", "joyful", "apprehensive", "caring", "proud", "emboldened", 
    "connected", "fulfilled", "refreshed", "supported", "affirmed", "nurtured", "reassured", 
    "invigorated", "centered", "uplifted", "calmly confident", "restored", "balanced", "validated"
]

activities = [
    "painting", "writing", "yoga", "meditation", "reading", "cooking", "gardening", "dancing", 
    "hiking", "journaling", "running", "swimming", "cycling", "drawing", "knitting", "singing", 
    "playing an instrument", "photography", "traveling", "volunteering", "shopping", "watching movies", 
    "listening to music", "baking", "making crafts", "visiting museums", "hanging out with friends", 
    "going to the gym", "doing puzzles", "binge-watching shows", "playing video games", "skating", 
    "cleaning", "meditative walking", "going to concerts", "exploring new places", "birdwatching", 
    "playing board games", "cycling in the park", "writing poetry", "trying new recipes", "attending workshops", 
    "rock climbing", "joining clubs", "volunteering at animal shelters", "crafting DIY projects", "fishing", 
    "making vision boards", "studying new languages", "attending live theater", "redecorating", "watching sports", 
    "deep breathing exercises", "taking mental health days", "talking to a therapist", "journaling about feelings", 
    "listening to guided meditations", "setting boundaries", "gratitude journaling", "doing affirmations", 
    "talking to loved ones", "volunteering for mental health causes", "practicing self-compassion", "seeking support groups"
]


# Generate unique datasets
def generate_datasets(num_samples=5000):  
    datasets = set()  # Use a set to avoid duplicates
    max_attempts = num_samples * 15  # Increase attempts for greater variation
    attempts = 0

    while len(datasets) < num_samples and attempts < max_attempts:
        theme = random.choice(list(templates.keys()))  
        user_template, bot_template = random.choice(templates[theme])
        
        user_input = user_template.format(
            emotion=random.choice(emotions),
            activity=random.choice(activities)
        )
        chatbot_response = bot_template.format(
            emotion=random.choice(emotions),
            activity=random.choice(activities))
        datasets.add((user_input, chatbot_response)) 
        attempts += 1

    return list(datasets)

# Save datasets to a CSV file
def save_to_csv(datasets, filename="mental_health_datasets5.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_ALL)  
        writer.writerow(["Patient's Context", "Psychiatrist's Response"])
        writer.writerows(datasets)

datasets = generate_datasets(30000)  
save_to_csv(datasets)

print(f"{len(datasets)} unique datasets generated and saved to 'mental_health_datasets4.csv'!")