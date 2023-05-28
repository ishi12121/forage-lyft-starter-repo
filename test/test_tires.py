import unittest
from tires.base import ArrayLengthException, InvalidDataPointException

from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires

class TestCarriganTires(unittest.TestCase):
  def test_all_under_threshold(self):
    """
    Test that it will return False
    when all tires' wear is under the threshold
    """
    sensor_data = [0, 0.2, 0.8, 0.5]
    test_tires = CarriganTires(sensor_data)
    self.assertFalse(test_tires.needs_service())

  def test_all_over_threshold(self):
    """
    Test that it will return True
    when all tires' wear is over the threshold
    """
    sensor_data = [0.9, 0.92, 1, 0.95]
    test_tires = CarriganTires(sensor_data)
    self.assertTrue(test_tires.needs_service())

  def test_one_over_threshold(self):
    """
    Test that it will return True
    when only one tire's wear is over the threshold
    """
    sensor_data = [0, 0.2, 0.95, 0.5]
    test_tires = CarriganTires(sensor_data)
    self.assertTrue(test_tires.needs_service())

  def test_all_at_threshold(self):
    """
    Test that it will return False
    when all tires' wear is at the threshold
    """
    sensor_data = [0.9, 0.9, 0.9, 0.9]
    test_tires = CarriganTires(sensor_data)
    self.assertTrue(test_tires.needs_service())

  def test_all_under_threshold(self):
    """
    Test that it will return False
    when all tires' wear is under the threshold
    """
    sensor_data = [0, 0.2, 0.8, 0.5]
    test_tires = CarriganTires(sensor_data)
    self.assertFalse(test_tires.needs_service())

  def test_three_values(self):
    """
    Test that it will raise an error
    when the sensor data includes less data points
    """
    sensor_data = [0, 0.2, 0.8]
    test_tires = CarriganTires(sensor_data)
    self.assertRaises(ArrayLengthException, test_tires.needs_service())

  def test_five_values(self):
    """
    Test that it will raise an error
    when the sensor data includes more data points
    """
    sensor_data = [0, 0.2, 0.8, 0.5, 0.1]
    test_tires = CarriganTires(sensor_data)
    self.assertRaises(ArrayLengthException, test_tires.needs_service())

  def test_below_bounds(self):
    """
    Test that it will raise an error
    when the sensor data includes a point less than 0
    """
    sensor_data = [0, 0.2, 0.8, -0.1]
    test_tires = CarriganTires(sensor_data)
    self.assertRaises(InvalidDataPointException, test_tires.needs_service())

  def test_above_bounds(self):
    """
    Test that it will raise an error
    when the sensor data includes a point greater than 1
    """
    sensor_data = [0, 0.2, 0.8, 1.1]
    test_tires = CarriganTires(sensor_data)
    self.assertRaises(InvalidDataPointException, test_tires.needs_service())

class TestOctoprimeTires(unittest.TestCase):
  def test_under_threshold(self):
    """
    Test that it will return False
    when sum of the tires' wear is under the threshold
    """
    sensor_data = [0, 0.2, 0.8, 0.5]
    test_tires = OctoprimeTires(sensor_data)
    self.assertFalse(test_tires.needs_service())

  def test_over_threshold(self):
    """
    Test that it will return True
    when sum of the tires' wear is over the threshold
    """
    sensor_data = [0.9, 0.92, 1, 0.95]
    test_tires = OctoprimeTires(sensor_data)
    self.assertTrue(test_tires.needs_service())

  def test_at_threshold(self):
    """
    Test that it will return False
    when all tires' wear is at the threshold
    """
    sensor_data = [0.7, 0.8, 0.7, 0.8]
    test_tires = OctoprimeTires(sensor_data)
    self.assertTrue(test_tires.needs_service())

  def test_three_values(self):
    """
    Test that it will raise an error
    when the sensor data includes less data points
    """
    sensor_data = [0, 0.2, 0.8]
    test_tires = OctoprimeTires(sensor_data)
    self.assertRaises(ArrayLengthException, test_tires.needs_service())

  def test_five_values(self):
    """
    Test that it will raise an error
    when the sensor data includes more data points
    """
    sensor_data = [0, 0.2, 0.8, 0.5, 0.1]
    test_tires = OctoprimeTires(sensor_data)
    self.assertRaises(ArrayLengthException, test_tires.needs_service())

  def test_below_bounds(self):
    """
    Test that it will raise an error
    when the sensor data includes a point less than 0
    """
    sensor_data = [0, 0.2, 0.8, -0.1]
    test_tires = OctoprimeTires(sensor_data)
    self.assertRaises(InvalidDataPointException, test_tires.needs_service())

  def test_above_bounds(self):
    """
    Test that it will raise an error
    when the sensor data includes a point greater than 1
    """
    sensor_data = [0, 0.2, 0.8, 1.1]
    test_tires = OctoprimeTires(sensor_data)
    self.assertRaises(InvalidDataPointException, test_tires.needs_service())