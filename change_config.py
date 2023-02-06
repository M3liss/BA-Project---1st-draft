import config

print(config.dataset_labels)
def add_label(label):
    config.add_dataset(label)

add_label("see")
print(config.dataset_labels)
