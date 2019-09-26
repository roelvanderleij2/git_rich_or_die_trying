import matplotlib.pyplot as plt

def copy_dictionary(dictionary):
    copy = {}

    for key in dictionary.keys():
        copy[key] = dictionary[key]

    return copy

def plot_performance(df, str_title, str_xaxis, str_yaxis):
    fig = plt.figure()
    plt.plot(df.index.values, df['Portfolio Value'])
    fig.suptitle(str_title, fontsize=18)
    plt.xlabel(str_xaxis, fontsize=12)
    plt.ylabel(str_yaxis, fontsize=12)
    plt.xticks(rotation=45)
