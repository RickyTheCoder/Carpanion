# Carpanion

## **Inspiration**

People driving alone experience many challenges, such as loneliness, boredom, and drowsiness. Drowsy drivers are incredibly dangerous and are estimated to contribute to 91,000 car crashes each year. Motivated by this alarming statistic, we created Carpanion, an AI companion designed to accompany and entertain users on their journeys. We aim to alleviate driver fatigue and minimize the risks of driving alone through lively conversation.

## **What it does**

Carpanion's main purpose is to engage the user in an interesting conversation, but some additional features to heighten the user's experience include customizing the companion's personality, debatably funny dad jokes, and interesting and useful information about the surrounding area, such as landmarks and local restaurants.

## **How we built it**

We combined the most recent advancements in natural language processing and machine learning with real-time data streaming from global positioning systems, made possible by object detection model YOLOv4, OpenAI's GPT-4 and Whisper models. Our tech stack uses Django's back end to handle the data processing and React Native for a responsive, user-friendly front end. We designed Carpanion to be a seamless blend of conversation and computation, delivering both safety and entertainment on the go.

## **Challenges we ran into**

We ran into some hurdles using OpenAI's software. It was particularly challenging to integrate Whisper for real-time speech-to-text capability, and much time and testing was put into Carpanion to make sure that GPT-4's responses were not only logical but also meaningful to the driver's surroundings. We also carefully designed a user interface and experience that would be streamlined, intuitive, and completely hands-free while driving.

## **Accomplishments that we're proud of**

A feature we're proud of is the ability to detect long silences from the user, which could be a sign of driver drowsiness, and respond with phrases to alert the driver of their potential drowsiness.

## **What we learned**

React Native was an entirely new language for us, but we decided to utilize it both for the learning experience and its compatibility with the AI tools that we wanted to include.

## **What's next for Carpanion**

We intend to improve its contextual awareness, add more languages and regional pronunciations to its commentary database, and enhance its interaction skills. Additionally, we hope to be able to implement a system similar to character.ai, where users can select a character or favorite personality to talk to, which would make drives even more entertaining.
