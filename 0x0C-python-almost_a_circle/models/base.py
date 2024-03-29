#!/usr/bin/python3
"""Defines a class Base."""


import json
import csv
import turtle


class Base:
    """Represents a class base."""

    __nb_objects = 0

    def __init__(self, id=None):
        """initiates the class with id
        public instance variable"""

        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """converts dictionary object to json"""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            new_list = []
            new_list.append(list_dictionaries[0])
            for i in range(1, len(list_dictionaries)):
                if list_dictionaries[i]["id"] == list_dictionaries[i-1]["id"]:
                    new_list[-1] = list_dictionaries[i]
                else:
                    new_list.append(list_dictionaries[i])
            return json.dumps(new_list)

    @staticmethod
    def from_json_string(json_string):
        """deserializes a json string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves file with json object"""
        if list_objs is not None:
            list_dict = [r.to_dictionary() for r in list_objs]
        else:
            list_dict = []
        with open("{}.json".format(cls.__name__), "w") as f:
            json_repr = cls.to_json_string(list_dict)
            f.write(json_repr)

    @classmethod
    def create(cls, **dictionary):
        """creates an instance of the class in
        question"""
        if cls.__name__ == "Square":
            instance = cls(size=1)
        elif cls.__name__ == "Rectangle":
            instance = cls(width=1, height=1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """loads a json file"""

        try:
            with open("{}.json".format(cls.__name__), "r") as f:
                list_dict = cls.from_json_string(f.read())
                list_instances = [cls.create(**dic) for dic in list_dict]
                return list_instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save a list of rect or square objects
        into a csv file"""

        with open(f"{cls.__name__}.csv", "w") as f:
            if list_objs is None or len(list_objs) == 0:
                f.write("[]")
            else:
                if cls.__name__ == "Square":
                    keys = ["id", "size", "x", "y"]
                elif cls.__name__ == "Rectangle":
                    keys = ["id", "width", "height", "x", "y"]
                csv_obj = csv.DictWriter(f, fieldnames=keys)
                for ins in list_objs:
                    csv_obj.writerow(ins.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """load csv file and return list of instances."""
        try:
            with open(f"{cls.__name__}.csv", "r") as f:
                if cls.__name__ == "Square":
                    keys = ["id", "size", "x", "y"]
                elif cls.__name__ == "Rectangle":
                    keys = ["id", "width", "height", "x", "y"]
                csvdict = csv.DictReader(f, fieldnames=keys)
                listdict = [{k: int(v) for k, v in d.items()} for d in csvdict]
                return [cls.create(**dic) for dic in listdict]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draw rectangles and squares based on
        their parameters using the turtle module"""

        myturtle = turtle.Turtle()
        myturtle.pensize(5)

        myturtle.color("blue")
        for rect in list_rectangles:
            myturtle.penup()
            myturtle.goto(rect.x, rect.y)
            myturtle.pendown()
            for _ in range(2):
                myturtle.forward(rect.width)
                myturtle.left(90)
                myturtle.forward(rect.height)
                myturtle.left(90)

        myturtle.color("purple")
        for sq in list_squares:
            myturtle.penup()
            myturtle.goto(sq.x, sq.y)
            myturtle.pendown()
            for _ in range(4):
                myturtle.forward(sq.size)
                myturtle.left(90)
        myturtle.hideturtle()
        turtle.exitonclick()
