# This code was written by Maya Schlesinger(maya.schlesinger@gmail.com)
# on 7/7/2016.
# This is a library for basic dealings with a 2d vector space (R^2)
import random
import math


def get_random_vector(x_min, x_max, y_min, y_max):
    """
    Returns a random vector from the 2d space within given limits.
    :param x_min: Int - The minimum x value.
    :param x_max: Int - The maximum x value.
    :param y_min: Int - The minimum y value.
    :param y_max: Int - The maximum y value.
    :return: Tuple (x,y) - A random vector from the 2d space.
    """
    return random.randrange(x_min, x_max), random.randrange(y_min, y_max)


def get_n_random_vectors(x_min, x_max, y_min, y_max, n):
    """
    Returns n random vectors from the 2d space within given limits.
    :param x_min: Int - The minimum x value.
    :param x_max: Int - The maximum x value.
    :param y_min: Int - The minimum y value.
    :param y_max: Int - The maximum y value.
    :param n: Int - The number of vectors to generate.
    :return: List of Tuples (x,y) - n random vectors from the 2d space.
    """
    return [get_random_vector(x_min, x_max, y_min, y_max) for i in range(n)]


def get_mass_center(vectors):
    """
    Returns the mass center of the given vector list.
    :param vectors: List of Tuples (x,y) - The vectors of which to calculate the mass center.
    :return: Tuple (x,y) - The mass center of the vectors.
    """
    sum_x = sum(vec[0] for vec in vectors)
    sum_y = sum(vec[1] for vec in vectors)
    n = len(vectors)
    return sum_x/n, sum_y/n


def calc_dist(vec1, vec2):
    """
    This method returns the distance between 2 vectors.
    :param vec1: Tuple (x,y) - The first vector.
    :param vec2: Tuple (x,y) - The second vector.
    :return: Double - The distance between the two vectors.
    """
    vec1_x, vec1_y = vec1
    vec2_x, vec2_y = vec2
    return math.sqrt((vec1_x-vec2_x)**2+(vec1_y-vec2_y)**2)


def calc_n_dists(vec, vec_list):
    """
    This method returns the distance between a vector and n vectors.
    :param vec: Tuple (x,y) - The vector.
    :param vec_list: List of Tuples (x,y) - The n vectors to caculate the distance from.
    :return: List of Doubles - At the index i is the distance between the vector and the vector at vec_list[i].
    """
    return [calc_dist(vec, other) for other in vec_list]


def get_closest_vec(vec, vec_list):
    """
    This method returns which of n vectors is closest to a specified vector.
    :param vec: Tuple (x,y) - The vector the return vector is closest to.
    :param vec_list: List of Tuples (x,y) - The n vectors from which to find the one closest to vec.
    :return: Int - The index of the closest vector to vec.
    """
    dists_list = calc_n_dists(vec, vec_list)
    return dists_list.index(min(dists_list))
