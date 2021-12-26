from unittest import TestCase
import view_utils

class Test(TestCase):
    def test_type_zodiac_info_html(self):
        response = view_utils.type_zodiac_info_html("fire")
        exp_html = """
    <ul>
        <li> <a href='Aries'>Aries </a> </li><li> <a href='Aries'>Aries </a> </li><li> <a href='Aries'>Aries </a> </li>
    <ul/>
    <ul>
        <li> <a href='Leo'>Leo </a> </li><li> <a href='Leo'>Leo </a> </li><li> <a href='Leo'>Leo </a> </li>
    <ul/>
    <ul>
        <li> <a href='Sagittarius'>Sagittarius </a> </li><li> <a href='Sagittarius'>Sagittarius </a> </li><li> <a href='Sagittarius'>Sagittarius </a> </li>
    <ul/>
"""
        self.assertEqual(exp_html, response)
        self.fail()
