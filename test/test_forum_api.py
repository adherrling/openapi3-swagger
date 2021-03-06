# coding: utf-8

"""
    Bungie.Net API

    These endpoints constitute the functionality exposed by Bungie.net, both for more traditional website functionality and for connectivity to Bungie video games and their related functionality.

    OpenAPI spec version: 3.0.0
    Contact: support@bungie.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.forum_api import ForumApi


class TestForumApi(unittest.TestCase):
    """ ForumApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.forum_api.ForumApi()

    def tearDown(self):
        pass

    def test_forum_approve_fireteam_thread(self):
        """
        Test case for forum_approve_fireteam_thread

        
        """
        pass

    def test_forum_get_core_topics_paged(self):
        """
        Test case for forum_get_core_topics_paged

        
        """
        pass

    def test_forum_get_forum_tag_suggestions(self):
        """
        Test case for forum_get_forum_tag_suggestions

        
        """
        pass

    def test_forum_get_poll(self):
        """
        Test case for forum_get_poll

        
        """
        pass

    def test_forum_get_post_and_parent(self):
        """
        Test case for forum_get_post_and_parent

        
        """
        pass

    def test_forum_get_post_and_parent_awaiting_approval(self):
        """
        Test case for forum_get_post_and_parent_awaiting_approval

        
        """
        pass

    def test_forum_get_posts_threaded_paged(self):
        """
        Test case for forum_get_posts_threaded_paged

        
        """
        pass

    def test_forum_get_posts_threaded_paged_from_child(self):
        """
        Test case for forum_get_posts_threaded_paged_from_child

        
        """
        pass

    def test_forum_get_recruitment_thread_summaries(self):
        """
        Test case for forum_get_recruitment_thread_summaries

        
        """
        pass

    def test_forum_get_topic_for_content(self):
        """
        Test case for forum_get_topic_for_content

        
        """
        pass

    def test_forum_get_topics_paged(self):
        """
        Test case for forum_get_topics_paged

        
        """
        pass

    def test_forum_join_fireteam_thread(self):
        """
        Test case for forum_join_fireteam_thread

        
        """
        pass

    def test_forum_kick_ban_fireteam_applicant(self):
        """
        Test case for forum_kick_ban_fireteam_applicant

        
        """
        pass

    def test_forum_leave_fireteam_thread(self):
        """
        Test case for forum_leave_fireteam_thread

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
