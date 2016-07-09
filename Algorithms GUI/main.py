# This code was written by Maya Schlesinger(maya.schlesinger@gmail.com)
# on 8/7/2016.
# This is a program to help visualize the KMeans clustering algorithm using GUI.
# It randomizes a few 2d vectors and then shows the clustering process.
import plane_gui
import clusters


class Main:
    """
    This class is used to manage the program.
    Each instance of this class will create a new window with 100 clusters(upper bound) and 1000 vectors.
    """
    CLUSTERS_NUM = 100
    VECTORS_NUM = 1000

    def __init__(self):
        self.window = plane_gui.Window(color_num=self.CLUSTERS_NUM, update_func=self.update)
        self.clustering_algo = clusters.KMeans.from_random_vectors(x_max=self.window.get_max_x(),
                                                                   y_max=self.window.get_max_y(),
                                                                   n=self.VECTORS_NUM, k=self.CLUSTERS_NUM)
        self.clustering_algo.start()
        self.window.draw_all_dots(self.clustering_algo.get_vectors_list(),
                                  self.clustering_algo.get_cluster_assignment())

    def update(self, e):
        """
        This does the next step of the algorithm abd then updates the GUI.
        :param e: This is meant to be a callback function, e is the event.
        """
        if self.clustering_algo.has_next():
            self.clustering_algo.next()
        self.window.clear()
        self.window.draw_all_dots(self.clustering_algo.get_vectors_list(),
                                  self.clustering_algo.get_cluster_assignment())
        self.window.draw_all_squares(self.clustering_algo.get_mass_centers(),
                                     range(self.clustering_algo.get_cluster_num()))

    def mainloop(self):
        """
        Start the GUI's mainloop.
        """
        self.window.mainloop()

if __name__ == "__main__":
    # Create an instance of the window.
    main = Main()
    # Call the mainloop.
    main.mainloop()
