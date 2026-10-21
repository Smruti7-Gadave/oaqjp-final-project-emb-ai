
import unittest
from emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):

    def test_anger(self):
        result = emotion_detector("I am very angry")
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_joy(self):
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_sadness(self):
        result = emotion_detector("I am sad about this")
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_fear(self):
        result = emotion_detector("I am afraid")
        self.assertEqual(result["dominant_emotion"], "fear")

    def test_disgust(self):
        result = emotion_detector("I feel disgusted")
        self.assertEqual(result["dominant_emotion"], "disgust")


if __name__ == "__main__":
    unittest.main()

