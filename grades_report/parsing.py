#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (c) 2020 KAUTH
"""


def check_grade_attributes(max_grade_str=None, passing_grade_str=None):
    """
    This function checks that:
    - The maximum grade and passing grade inputs are numbers
    - The passing grade is smaller or equal to the maximum grade

    The function also assigns the default values to maximum and passing grade,
    if they are not defined by the user's input.

    :param max_grade_str: the input string from the user for the maximum grade
    :param passing_grade_str: the input string from the user for the passing
    grade
    :return grade_attributes: a dictionary with the maximum grade and passing
    grade values
    """
    if max_grade_str is not None:

        try:
            max_grade = float(max_grade_str)

        except ValueError:
            error = f"\nError: {max_grade_str} is not a number!"
            print(error)

            return error

    if passing_grade_str is not None:

        try:
            passing_grade = float(passing_grade_str)

        except ValueError:
            error = f"\nError: {passing_grade_str} is not a number!"
            print(error)

            return error

    if max_grade_str is not None and passing_grade_str is not None:

        if max_grade <= 0 or passing_grade <= 0:
            error = (
                "\nError: Maximum and passing grade cannot be smaller or " +
                "equal to zero!"
            )
            print(error)

            return error

        if passing_grade > max_grade:
            error = (
                "\nError: Passing grade cannot be greater than the maximum " +
                "grade!"
            )
            print(error)

            return error

    if max_grade_str is None and passing_grade_str is None:
        max_grade = 10
        passing_grade = max_grade / 2

    if max_grade_str is not None and passing_grade_str is None:
        passing_grade = max_grade / 2

    if max_grade_str is None and passing_grade_str is not None:
        max_grade = 2 * passing_grade

    grade_attributes = {"max_grade": max_grade, "passing_grade": passing_grade}

    return grade_attributes


def check_grades_list(unchecked_list, max_grade):
    """
    This function checks that the given list contains elements with the
    accepted format and rules.

    :param unchecked_list: the list that is generated after parsing the given
    file of grades or the list that is given directly as a string input by the
    user from the CLI
    :param max_grade: the maximum grade that you can score
    :return checked_list: the parsed list that can be given to calculate the
    grade statistics
    """
    checked_list = list()

    if type(unchecked_list) is str:
        unchecked_list = unchecked_list.strip('][').split(',')

    for item in unchecked_list:

        try:
            item = float(item)

        except ValueError:
            error = f"\nError: {item} is not a number!"
            print(error)

            return error

        if item < 0:
            error = f"\nError: {item} is not a positive number!"
            print(error)

            return error

        if item > max_grade:
            error = f"\nError: {item} is a number greater than the max grade!"
            print(error)

            return error

        checked_list.append(item)

    return checked_list


def check_personal_grade(personal_grade):
    """
    This function checks that the personal grade has the appropriate format.

    :param personal_grade: the input string from the user for his personal
    grade
    """
    try:
        personal_grade = float(personal_grade)

    except ValueError:
        error = f"\nError: {personal_grade} is not a number!"
        print(error)

        return error

    return personal_grade


def parse_user_input(
    grades_list, max_grade_str, passing_grade_str, personal_grade
):
    """
    This function checks that the user's input is in the correct format and
    returns the user's input after the appropriate preprocessing.

    :param grades_list: the input string from the user for the list of grades
    :param max_grade_str: the input string from the user for the maximum grade
    :param passing_grade_str: the input string from the user for the passing
    grade
    :param personal_grade: the input string from the user for his personal
    grade
    :return user_input: a dictionary with the values of the user's input after
    the appropriate validation
    """
    grade_attributes = check_grade_attributes(max_grade_str, passing_grade_str)

    try:
        max_grade = grade_attributes["max_grade"]
        passing_grade = grade_attributes["passing_grade"]

    except TypeError:
        max_grade = None
        passing_grade = None

    if grades_list != "False":
        checked_list = check_grades_list(grades_list, max_grade)

    else:
        error = "\nError: You must provide a list of grades!"
        print(error)

        checked_list = None

    if personal_grade != 0:
        personal_grade = check_personal_grade(personal_grade)

    else:
        personal_grade = None

    user_input = {
        "checked_list": checked_list,
        "max_grade": max_grade,
        "passing_grade": passing_grade,
        "personal_grade": personal_grade
    }

    return user_input
