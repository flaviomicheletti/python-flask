import run
import unittest


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        run.app.config["TESTING"] = True
        self.app = run.app.test_client()

    def test_acessando_paginas(self):
        print("index")
        self.app.get("/")
        print("\nbase2")
        self.app.get("/posts/base2")
        print("\nindex")
        self.app.get("/")
        print("\nbase3")
        self.app.get("/posts/base3")
        print("\nbase1")
        self.app.get("/posts/base1")
        print("\nbase2")
        self.app.get("/posts/base2")
        print("\nindex")
        self.app.get("/")
        print("\nprod")
        self.app.get("/posts/prod")
        print("\ndev")
        self.app.get("/posts/dev")
        print("\nindex")
        self.app.get("")
        print("\nbase3")
        self.app.get("/posts/base3")


if __name__ == "__main__":
    unittest.main()
