# This code was written by Maya Schlesinger(maya.schlesinger@gmail.com)
# on 7/7/2016.
# This is a library for dealing with clusters and clustering algorithms.
import plane_space
import abc
import random


class ClusteringClass(metaclass=abc.ABCMeta):
    """
    This class is an abstract base class for implemented and tracking of
    clustering algorithms, any clustering algorithm is to be implemented
    in a class inheriting from this one.
    """
    DEFAULT_X_MIN = 0
    DEFAULT_Y_MIN = 0
    DEFAULT_X_MAX = 100
    DEFAULT_Y_MAX = 100
    DEFAULT_N = 1000
    DEFAULT_K = 10

    def __init__(self, list_of_vectors, k):
        """
        :param list_of_vectors: List of Tuples (x,y) - The vectors to be clustered.
        :param k: Int - The number of clusters to create(upper bound).
        """
        self.vectors_num = len(list_of_vectors)
        self.cluster_num = k
        self.vectors = list_of_vectors
        self.cluster_assignment = [0] * self.vectors_num

    @classmethod
    def from_random_vectors(cls, x_min=DEFAULT_X_MIN,
                            x_max=DEFAULT_X_MAX, y_min=DEFAULT_Y_MIN,
                            y_max=DEFAULT_Y_MAX, n=DEFAULT_N, k=DEFAULT_K):
        """
        This factory class method creates a random list of vectors to be clustered.
        parameters will be given default values if not specified.
        :param x_min: The minimum x value of the vectors being clustered.
        :param x_max: Int - The maximum x value of the vectors being clustered.
        :param y_min: Int - The minimum y value of the vectors being clustered.
        :param y_max: Int - The maximum y value of the vectors being clustered.
        :param n: Int - The number of vectors to be clustered.
        :param k: Int - The number of clusters to create(uppper bound).
        """
        list_of_vectors = plane_space.get_n_random_vectors(x_min, x_max, y_min, y_max, n)
        return cls(list_of_vectors, k)

    def get_vectors_list(self):
        """
        :return: List of Tuples (x,y) - The vectors being clustered.
        """
        return self.vectors

    def get_cluster_assignment(self):
        """
        :return: List of Int - The cluster assignment, the dot with index i
        is assigned the cluster at index i of the list.
        """
        return self.cluster_assignment

    def random_cluster_assignments(self):
        """
        This method assigns the vectors to clusters randomly.
        """
        for i in range(self.vectors_num):
            self.cluster_assignment[i] = random.randrange(0, self.cluster_num)

    def get_cluster_num(self):
        """
        :return: Int - The number of clusters.
        """
        return self.cluster_num

    def get_cluster(self, cluster_index):
        """
        This method returns a cluster
        :param cluster_index: Int - The number of the cluster.
        :return: List of Tuples (x,y) - The vectors in the cluster.
        """
        return [self.vectors[i] for i in range(self.vectors_num) if self.cluster_assignment[i] == cluster_index]

    @abc.abstractmethod
    def start(self):
        """
        This method initializes the clustering algorithm.
        """

    @abc.abstractmethod
    def next(self):
        """
        This method does another step of clustering.
        """

    @abc.abstractmethod
    def has_next(self):
        """
        This method tests if the algorithm is done. If there is another step to be taken.
        :return: Boolean - Whether or not the algorithm is done. If so the "end()" method should be called.
        """

    @abc.abstractmethod
    def end(self):
        """
        This method finishes the algorithms actions.
        """


class KMeans(ClusteringClass):
    """
    This class is used to track and activate the clustering algorithm KMeans.
    """
    def __init__(self, list_of_vectors, k):
        super(KMeans, self).__init__(list_of_vectors, k)
        self.mass_centers = []

    def update_mass_centers(self):
        """
        This method calculates and updates the mass centers of the clusters.
        """
        self.mass_centers = []
        for i in range(self.cluster_num):
            try:
                self.mass_centers.append(plane_space.get_mass_center(self.get_cluster(i)))
            except ZeroDivisionError:
                print("Lost a cluster!")

    def update_vec_cluster_assignment(self, vec_index):
        """
        This method calculates and updates the cluster assignment for a given vector.
        :param vec_index: Int - The index of the vector in the vector list.
        """
        self.cluster_assignment[vec_index] = plane_space.get_closest_vec(self.vectors[vec_index], self.mass_centers)

    def update_cluster_assignment(self):
        """
        This method updates the cluster assignments for all vectors.
        """
        for i in range(self.vectors_num):
            self.update_vec_cluster_assignment(i)

    def start(self):
        self.random_cluster_assignments()
        self.update_mass_centers()

    def has_next(self):
        return True

    def next(self):
        self.update_mass_centers()
        self.update_cluster_assignment()

    def get_mass_centers(self):
        return self.mass_centers

    def end(self):
        pass
