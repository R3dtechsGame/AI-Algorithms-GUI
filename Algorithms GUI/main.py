import plane_gui
import clusters


class Main:
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
        if self.clustering_algo.has_next():
            self.clustering_algo.next()
        self.window.clear()
        self.window.draw_all_dots(self.clustering_algo.get_vectors_list(),
                                  self.clustering_algo.get_cluster_assignment())
        self.window.draw_all_squares(self.clustering_algo.get_mass_centers(),
                                     range(self.clustering_algo.get_cluster_num()))

    def mainloop(self):
        self.window.mainloop()

if __name__ == "__main__":
    main = Main()
    main.mainloop()
