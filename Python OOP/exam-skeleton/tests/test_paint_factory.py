import unittest
from project.factory.paint_factory import PaintFactory


class TestPaintFactory(unittest.TestCase):
    def setUp(self):
        self.paint_factory = PaintFactory("pobeda", 21)

    def test_init_class_initialize_exact_properties(self):
        self.assertEqual(self.paint_factory.name, "pobeda")
        self.assertEqual(self.paint_factory.capacity, 21)
        self.assertEqual(self.paint_factory.ingredients, {})
        self.assertEqual(self.paint_factory.__class__.__name__, "PaintFactory")

    def test_factory_class_can_add_method(self):
        self.assertFalse(self.paint_factory.can_add(22))

    def test_add_ingredients_when_properly_added(self):
        self.paint_factory.add_ingredient("blue", 7)
        self.assertEqual(self.paint_factory.ingredients["blue"], 7)

    def test_add_ingredients_when_not_properly_added(self):
        with self.assertRaisesRegex(TypeError, f"Ingredient of type sinio not allowed in {self.paint_factory.__class__.__name__}"):
            self.paint_factory.add_ingredient("sinio", 7)

    def test_remove_ingredients_when_proper_arguments_added(self):
        self.paint_factory.add_ingredient("blue", 7)
        self.paint_factory.remove_ingredient("blue", 7)
        self.assertEqual(self.paint_factory.ingredients.capacity, 21)

    def test_remove_ingredients_when_wrong_arguments_added(self):
        with self.assertRaisesRegex(TypeError, f"Ingredient of type sinio not allowed in {self.paint_factory.__class__.__name__}"):
            self.paint_factory.remove_ingredient("sinio", 7)

    def test_report(self):
        self.paint_factory.add_ingredient("blue", 7)
        exp_result = "Factory name: pobeda with capacity 14.\nblue: 7\n"
        result = self.paint_factory
        self.assertEqual(str(result), exp_result)

    def test_return_property(self):
        self.paint_factory.add_ingredient("blue", 7)
        self.assertEqual(self.paint_factory.products, {"blue": 7})


if __name__ == "__main__":
    unittest.main()
