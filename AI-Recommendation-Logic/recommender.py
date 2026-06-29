recommendation_data = {

    "Programming": {

        "Beginner": [
            "Python Basics",
            "HTML & CSS",
            "Git & GitHub",
            "JavaScript Fundamentals"
        ],

        "Intermediate": [
            "Flask",
            "React",
            "SQL",
            "REST APIs"
        ],

        "Advanced": [
            "System Design",
            "Docker",
            "Kubernetes",
            "Machine Learning"
        ]

    },

    "Movies": {

        "Beginner": [
            "The Matrix",
            "Interstellar",
            "Inception",
            "Avatar"
        ],

        "Intermediate": [
            "Shutter Island",
            "Tenet",
            "The Prestige",
            "Arrival"
        ],

        "Advanced": [
            "Memento",
            "Primer",
            "Predestination",
            "Coherence"
        ]

    },

    "Books": {

        "Beginner": [
            "Atomic Habits",
            "The Alchemist",
            "Rich Dad Poor Dad",
            "Think Like a Monk"
        ],

        "Intermediate": [
            "Clean Code",
            "Deep Work",
            "The Pragmatic Programmer",
            "The Psychology of Money"
        ],

        "Advanced": [
            "Design Patterns",
            "Artificial Intelligence",
            "Deep Learning",
            "Algorithms"
        ]

    },

    "Music": {

        "Beginner": [
            "Pop Playlist",
            "Soft Rock",
            "Lo-Fi",
            "Acoustic Hits"
        ],

        "Intermediate": [
            "Jazz Classics",
            "Indie Rock",
            "Electronic Mix",
            "Alternative"
        ],

        "Advanced": [
            "Classical Symphony",
            "Progressive Rock",
            "Fusion Jazz",
            "Instrumental Collection"
        ]

    },

    "Sports": {

        "Beginner": [
            "Walking",
            "Badminton",
            "Cycling",
            "Yoga"
        ],

        "Intermediate": [
            "Football",
            "Cricket",
            "Swimming",
            "Volleyball"
        ],

        "Advanced": [
            "Marathon",
            "CrossFit",
            "Triathlon",
            "Powerlifting"
        ]

    }

}


def get_recommendations(category, level):

    if category in recommendation_data:
        if level in recommendation_data[category]:
            return recommendation_data[category][level]

    return ["No recommendations available."]
