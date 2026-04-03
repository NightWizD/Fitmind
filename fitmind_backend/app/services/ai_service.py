import openai
import json
from typing import Dict, Any
import os

# Set OpenAI API key
openai.api_key = "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"

async def generate_workout_plan(user_data: Dict[str, Any], training_preferences: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generate a personalized workout plan using OpenAI based on user data and preferences.

    Args:
        user_data: Dict containing age, gender, height, weight, goal, activity_level, bmi
        training_preferences: Dict containing gym_access, days_per_week, hours_per_session

    Returns:
        Dict with structured workout plan
    """

    # Calculate BMI category
    bmi = user_data.get('bmi', 22.5)
    if bmi < 18.5:
        bmi_category = "Underweight"
    elif bmi < 25:
        bmi_category = "Normal"
    elif bmi < 30:
        bmi_category = "Overweight"
    else:
        bmi_category = "Obese"

    # Craft the prompt
    prompt = f"""
    Generate a personalized workout plan for a user with the following profile:

    Age: {user_data.get('age', 25)}
    Gender: {user_data.get('gender', 'Male')}
    BMI: {bmi:.1f} ({bmi_category})
    Goal: {user_data.get('goal', 'General Fitness')}
    Activity Level: {user_data.get('activity_level', 'Moderately Active')}
    Gym Access: {'Yes' if training_preferences.get('gym_access', True) else 'No'}
    Days per week: {training_preferences.get('days_per_week', 3)}
    Hours per session: {training_preferences.get('hours_per_session', 1)}

    Please generate a structured workout plan in JSON format only. Do not include any text outside the JSON.

    The JSON should have this structure:
    {{
      "weekly_split": "Description of the weekly split",
      "days": [
        {{
          "day": "Monday",
          "focus": "Muscle group focus",
          "exercises": [
            {{
              "name": "Exercise Name",
              "sets": 3,
              "reps": "10-12"
            }}
          ]
        }}
      ]
    }}

    Ensure the plan is safe, progressive, and suitable for the user's profile. Include rest days appropriately.
    """

    try:
        response = await openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a professional fitness trainer. Generate workout plans in JSON format only."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=2000,
            temperature=0.7
        )

        content = response.choices[0].message.content.strip()

        # Try to parse as JSON
        plan = json.loads(content)

        # Validate structure
        if not isinstance(plan, dict) or 'days' not in plan or 'weekly_split' not in plan:
            raise ValueError("Invalid plan structure")

        return plan

    except json.JSONDecodeError:
        raise ValueError("AI response is not valid JSON")
    except Exception as e:
        raise ValueError(f"Error generating workout plan: {str(e)}")
