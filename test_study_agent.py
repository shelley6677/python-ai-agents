import unittest

from study_agent import StudyAgent


class TestStudyAgent(unittest.TestCase):
    def setUp(self):
        self.agent = StudyAgent("Test Coach")

    def test_agent_name(self):
        self.assertEqual(self.agent.name, "Test Coach")

    def test_motivate(self):
        result = self.agent.motivate()

        self.assertEqual(
            result,
            "Small, consistent progress leads to big results!"
        )

    def test_empty_progress(self):
        result = self.agent.show_progress()

        self.assertEqual(
            result,
            "You have not completed any tasks yet."
        )

    def test_progress_with_tasks(self):
        self.agent.completed_tasks.append("Practice functions")
        self.agent.completed_tasks.append("Practice dictionaries")

        result = self.agent.show_progress()

        self.assertIn("1. Practice functions", result)
        self.assertIn("2. Practice dictionaries", result)

    def test_unknown_command(self):
        result = self.agent.respond("dance")

        self.assertEqual(
            result,
            "I do not understand that command."
        )

    def test_command_ignores_capitalization_and_spaces(self):
        result = self.agent.respond("  MOTIVATE  ")

        self.assertEqual(
            result,
            "Small, consistent progress leads to big results!"
        )
    def test_goal_command(self):
        result = self.agent.respond("goal")

        self.assertEqual(
            result,
            "My goal is to help you practice Python consistently."
        )

if __name__ == "__main__":
    unittest.main()