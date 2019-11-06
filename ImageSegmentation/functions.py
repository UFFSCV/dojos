from matplotlib import pyplot as plt

def plot(images, titles, cmap):
    for i in range(len(images)):
        plt.subplot(2, 3, i+1)
        plt.imshow(images[i], cmap=cmap)
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()
