"""Concept Coach v1, Epic 9 - Student Progress Views."""

import inspect
import json
import os
import pytest
import unittest

from pastasauce import PastaSauce, PastaDecorator
from random import randint  # NOQA
from selenium.webdriver.common.by import By  # NOQA
from selenium.webdriver.support import expected_conditions as expect  # NOQA
from staxing.assignment import Assignment  # NOQA

# select user types: Admin, ContentQA, Teacher, and/or Student
from staxing.helper import Student  # NOQA

basic_test_env = json.dumps([{
    'platform': 'OS X 10.11',
    'browserName': 'chrome',
    'version': '50.0',
    'screenResolution': "1024x768",
}])
BROWSERS = json.loads(os.getenv('BROWSERS', basic_test_env))
TESTS = os.getenv(
    'CASELIST',
    str([7732, 7733, 7735, 7736, 7737])  # NOQA
)


@PastaDecorator.on_platforms(BROWSERS)
class TestEpicName(unittest.TestCase):
    """CC1.09 - Student Progress Views."""

    def setUp(self):
        """Pretest settings."""
        self.ps = PastaSauce()
        self.desired_capabilities['name'] = self.id()
        self.Teacher = Teacher(
            use_env_vars=True,
            pasta_user=self.ps,
            capabilities=self.desired_capabilities
        )

    def tearDown(self):
        """Test destructor."""
        self.ps.update_job(job_id=str(self.teacher.driver.session_id),
                           **self.ps.test_updates)
        try:
            self.teacher.delete()
        except:
            pass

    # Case C7732 - 001 - Student | View section completion report
    @pytest.mark.skipif(str(7732) not in TESTS, reason='Excluded')  # NOQA
    def test_usertype_story_text(self):
        """View section completion report.

        Steps: 

        Go to https://tutor-staging.openstax.org/
        Click on the 'Login' button
        Enter the student user account in the username and password text boxes
        Click on the 'Sign in' button
        If the user has more than one course, click on a Concept Coach course name

        Click on "Contents"
        Select a section 
        Scroll to bottom of the section
        Click "Launch Concept Coach" 
        Enter a response into the free response text box
        Click "Answer"
        Select a multiple choice answer
        Click "Submit"
        Click "Next question" 
        Continue answering questions


        Expected Result:

        The user is presented with section completion report that shows "You're done"

        """
        self.ps.test_updates['name'] = 'cc1.09.001' \
            + inspect.currentframe().f_code.co_name[4:]
        self.ps.test_updates['tags'] = [
            'cc1',
            'cc1.09',
            'cc1.09.001',
            '7732'
        ]
        self.ps.test_updates['passed'] = False

        # Test steps and verification assertions

        self.ps.test_updates['passed'] = True


    # Case C7733 - 002 - Student | Completion report shows the section status of started and completed modules
    @pytest.mark.skipif(str(7733) not in TESTS, reason='Excluded')  # NOQA
    def test_usertype_story_text(self):
        """Completion report shows the section status of started and completed modules.

        Steps: 

        Click on "Contents"
        Select a section 
        Scroll to bottom of the section
        Click "Launch Concept Coach" 
        Enter a response into the free response text box
        Click "Answer"
        Select a multiple choice answer
        Click "Submit"
        Click "Next question" 
        Continue answering questions


        Expected Result:

        The user is presented with the completion report, which shows the section status of completed modules

        """
        self.ps.test_updates['name'] = 'cc1.09.002' \
            + inspect.currentframe().f_code.co_name[4:]
        self.ps.test_updates['tags'] = [
            'cc1',
            'cc1.09',
            'cc1.09.002',
            '7733'
        ]
        self.ps.test_updates['passed'] = False

        # Test steps and verification assertions

        self.ps.test_updates['passed'] = True


    # Case C7735 - 003 - Student | Able to access the progress views at any point
    @pytest.mark.skipif(str(7735) not in TESTS, reason='Excluded')  # NOQA
    def test_usertype_story_text(self):
        """Able to access the progress views at any point.

        Steps: 

        Click on "Contents"
        Select a section 
        Scroll to bottom of the section
        Click "Launch Concept Coach" 
        Click "My Progress" in the header


        Expected Result:

        The user is presented with the progress view

        """
        self.ps.test_updates['name'] = 'cc1.09.003' \
            + inspect.currentframe().f_code.co_name[4:]
        self.ps.test_updates['tags'] = [
            'cc1',
            'cc1.09',
            'cc1.09.003',
            '7735'
        ]
        self.ps.test_updates['passed'] = False

        # Test steps and verification assertions

        self.ps.test_updates['passed'] = True


    # Case C7736 - 004 - Student | Return to current position in an assignment
    @pytest.mark.skipif(str(7736) not in TESTS, reason='Excluded')  # NOQA
    def test_usertype_story_text(self):
        """Return to current position in an assignment.

        Steps: 

        Click on "Contents"
        Select a section 
        Scroll to bottom of the section
        Click "Launch Concept Coach" 
        Enter a response into the free response text box
        Click "Answer"
        Select a multiple choice answer
        Click "Submit"
        Click "Next question"

        Click "Close" in the right corner of the header
        Click "Launch Concept Coach"


        Expected Result:

        The user is presented with their current position in the assignment

        """
        raise NotImplementedError(inspect.currentframe().f_code.co_name)


    # Case C7737 - 005 - Student | Able to review previous modules
    @pytest.mark.skipif(str(7737) not in TESTS, reason='Excluded')  # NOQA
    def test_usertype_story_text(self):
        """Able to review previous modules.

        Steps: 

        Click on "Contents"
        Select a section 
        Scroll to bottom of the section
        Click "Launch Concept Coach" 
        Click "My Progress" in the header
        Click on the desired module under the "Previous" section


        Expected Result:

        The user is presented with a previous module

        """
        self.ps.test_updates['name'] = 'cc1.09.005' \
            + inspect.currentframe().f_code.co_name[4:]
        self.ps.test_updates['tags'] = [
            'cc1',
            'cc1.09',
            'cc1.09.005',
            '7737'
        ]
        self.ps.test_updates['passed'] = False

        # Test steps and verification assertions

        self.ps.test_updates['passed'] = True