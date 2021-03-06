import os
import numpy as np
import torch as tc
import matplotlib.pyplot as plt
from scipy.special import gamma
from matplotlib.backends.backend_pdf import PdfPages

from mtplt.utils.data_util import sort_y, get_axis_tick


CURR_PATH = os.path.split(os.path.realpath(__file__))[0]


def render(save_pdf: bool, figure_name: str):
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    if save_pdf:
        pdf = PdfPages(os.path.join(CURR_PATH, f'{figure_name}.pdf'))
        pdf.savefig()
        plt.close()
        pdf.close()
    else:
        plt.title(figure_name, pad=30)
        plt.show()


def paint_segments(save_pdf: bool):
    x1 = [147.7, 192.5, 257.3]
    y1 = [32.1, 36.4, 38.6]
    
    x2 = [147.7, 192.5, 257.3]
    y2 = [33.4, 37.4, 39.5]
    
    x3 = [147.7, 192.5, 257.3]
    y3 = [33.8, 38.3, 40.2]
    
    x4 = [195.4, 260.7]
    y4 = [37.9, 40.6]
    
    x5 = [195.4, 260.7]
    y5 = [38.9, 41.5]
    
    x6 = [121.4]
    y6 = [32.2]
    
    x7 = [121.4]
    y7 = [33.5]
    
    plt.figure()
    plt.plot(x1, y1, label='ResNet', c='lightblue', mec='lightblue', mfc='lightblue',
             marker='o', ls='-', ms=8, lw=1.2)
    plt.plot(x2, y2, label='SCR-ResNet', c='deepskyblue', mec='deepskyblue', mfc='white',
             marker='o', ls=(0, (6, 2)), ms=8, lw=1.2)
    # pyplt.plot(x3, y3, label='ResNet-HS', c='steelblue', mec='steelblue', mfc='white',
    # 		 marker='o', ls=(0, (6, 2)), ms=8, lw=1.2)
    
    plt.plot(x4, y4, label='ResNeXt', c='lightcoral', mec='lightcoral', mfc='lightcoral',
             marker='s', ls='-', ms=9, linewidth=1.2)
    plt.plot(x5, y5, label='SCR-ResNeXt', c='red', mec='red', mfc='white',
             marker='s', ls=(0, (6, 2)), ms=8, lw=1.2)
    
    plt.plot(x6, y6, label='MobileNetV2', c='yellowgreen', mec='yellowgreen', mfc='yellowgreen',
             marker='^', ls=(0, (6, 2)), ms=8, linewidth=1.2)
    plt.plot(x7, y7, label='SCR-MobileNetV2', c='olivedrab', mec='olivedrab', mfc='white',
             marker='^', ls=(0, (6, 2)), ms=8, lw=1.2)
    
    x_bg, x_ed = 100, 270
    plt.xlabel('FLOPs(G)')
    plt.xlim(x_bg, x_ed)
    vals, texts = get_axis_tick(x_bg, x_ed, 20)
    plt.xticks(vals, texts)
    
    y_bg, y_ed = 30.0, 42.0
    plt.ylabel('AP')
    plt.ylim(y_bg, y_ed)
    vals, texts = get_axis_tick(y_bg, y_ed, 2.0)
    plt.yticks(vals, texts)
    
    plt.legend(loc='lower right', title='SCR-Backbone(stage)')
    render(save_pdf, 'pic_line')


def paint_scatters(save_pdf: bool):
    y1 = [36.45,
          37.11,
          36.89,
          36.83,
          37.35,
          37.74,
          36.94,
          37.8,
          38.3,
          38, ]
    x1 = [76.498,
          76.454,
          75.858,
          76.05,
          75.874,
          75.888,
          75.252,
          76.34,
          76.47,
          76.3, ]
    
    y2 = [38.6,
          39.03,
          39.5,
          40,
          39.2,
          39,
          39.4,
          40.2, ]
    x2 = [77.37,
          77.61,
          77.74,
          77.19,
          77.11,
          77.19,
          77.38,
          77.26, ]
    
    x1, y1 = sort_y(x1, y1)
    x2, y2 = sort_y(x2, y2)
    
    assert (len(x1) and len(x2))
    x1_max, y1_max = [x1[-1]], [y1[-1]]
    x2_max, y2_max = [x2[-1]], [y2[-1]]
    x1, y1 = x1[:-1], y1[:-1]
    x2, y2 = x2[:-1], y2[:-1]
    
    plt.scatter(x1, y1, label='R50 FLOPs', s=82, ec='black', fc='tomato', marker='o', lw=0.8)
    plt.scatter(x1_max, y1_max, label='R50 FLOPs (best)', s=90, ec='black', fc='tomato', marker='^', lw=0.8)
    
    plt.scatter(x2, y2, label='R101 FLOPs', s=78, ec='black', fc='skyblue', marker='s', lw=0.8)
    plt.scatter(x2_max, y2_max, label='R101 FLOPs (best)', s=150, ec='black', fc='skyblue', marker='*', lw=0.8)
    plt.annotate("(%.1f, %.1f)" % (x1_max[0], y1_max[0]), xy=(x1_max[0], y1_max[0]),
                 xytext=(x1_max[0] - 0.268, y1_max[0] + 0.17))
    plt.annotate("(%.1f, %.1f)" % (x2_max[0], y2_max[0]), xy=(x2_max[0], y2_max[0]),
                 xytext=(x2_max[0] - 0.268, y2_max[0] + 0.17))
    
    # pyplt.grid(True, c='silver')
    
    x_bg, x_ed = 75.0, 78.0
    plt.xlabel('Top1 Acc.')
    plt.xlim(x_bg, x_ed)
    vals, texts = get_axis_tick(x_bg, x_ed, 0.5)
    plt.xticks(vals, texts)
    # pyplt.gca().xaxis.set_minor_locator(pyplt.IndexLocator(base=x_bg, offset=0.5))
    
    y_bg, y_ed = 36.0, 41.0
    plt.ylabel('AP')
    plt.ylim(y_bg, y_ed)
    vals, texts = get_axis_tick(y_bg, y_ed, 1.0)
    plt.yticks(vals, texts)
    # pyplt.gca().yaxis.set_minor_locator(pyplt.IndexLocator(base=y_bg, offset=1))
    
    plt.legend(loc='lower right', title=' FLOPs equivalent ')
    render(save_pdf, 'pic_point')


def paint_func(save_pdf: bool):
    x = tc.linspace(-3, 3, 1000)
    
    se = (x - 1) * (x - 1)
    
    ideal = tc.zeros(1000)
    for i in range(500):
        ideal[i] += 1
    
    hinge = -(x - 1)
    for i in range(1000):
        if hinge[i] <= 0:
            hinge[i] = 0
    
    sig = tc.sigmoid(x) - 1
    sig = sig * sig
    
    ce = np.exp(-1 * np.linspace(-2.5, 2.5, 1000)) + 1
    ce = np.log(ce)
    ce = tc.from_numpy(ce) / np.log(2)
    
    plt.figure()
    plt.grid(True)
    plt.plot(x, ideal, label='Ideal Error', c='black', ls='-', lw=2)
    plt.plot(x, se, label='Square Error', c='steelblue', ls='-', lw=2)
    plt.plot(x, ce, label='Log Sigmoid', c='tomato', ls='-', lw=2)
    plt.plot(x, hinge, label='Hinge', c='forestgreen', ls='-', lw=2)
    plt.plot(x, sig, label='Sigmoid Square', c='orange', ls='-', lw=2)
    
    plt.xlabel('g(x)*f(x)')
    plt.ylabel('loss')
    
    plt.ylim(0, 2.5)
    
    plt.legend(loc='best', title='loss')
    render(save_pdf, 'pic_func')


def paint_gaussian(save_pdf: bool):
    mu, sigma = 0, 1
    x = tc.linspace(mu-3*sigma, mu+3*sigma, 1024)
    
    gp = tc.exp(-((x - mu)**2) / (2*sigma**2)) / (sigma * np.sqrt(2*np.pi))
    sig_gp = tc.sigmoid(gp) - 0.5

    plt.figure()
    plt.grid(True)
    plt.plot(x, gp, label='Gaussian', c='black', ls='-', lw=1)
    plt.plot(x, sig_gp, label='Sigmoid Gaussian', c='steelblue', ls='-', lw=1)

    plt.xlabel('x')
    plt.ylabel('y')

    plt.legend(loc='best', title='PDF')
    render(save_pdf, 'pic_gaussian')


def paint_generalized_gaussian(save_pdf: bool):
    # https://en.wikipedia.org/wiki/Generalized_normal_distribution
    mu, sigma = 0, 1
    x = tc.linspace(mu-3*sigma, mu+3*sigma, 1024)
    
    plt.figure()
    plt.grid(True)
    
    properties = [
        (1, 'Laplace', 'tomato'),
        (2, 'Gaussian', 'orange'),
        (4, 'Almost Gaussian', 'forestgreen'),
        (8, 'Median', 'steelblue'),
        (1024, 'Almost Uniform', 'purple'),
    ]
    for beta, name, color in properties:
        alpha = sigma * np.sqrt(gamma(1/beta) / gamma(3/beta))
        gp = beta / (2 * alpha * gamma(1./beta)) * tc.exp(-tc.pow(tc.abs(x-mu)/alpha, beta))
        plt.plot(x, gp, label=r'$\beta$={}: {}'.format(beta, name), c=color, ls='-', lw=1)
    
    plt.xlabel('x')
    plt.ylabel('y')
    
    plt.legend(loc='best', title='PDF')
    render(save_pdf, 'pic_g_gaussian')


def paint_hot(save_pdf: bool):
    
    render(save_pdf, 'pic_hot')


def main():
    chosen = 'ggau'
    save_pdf = False
    
    paint = {
        'sca': paint_scatters,
        'func': paint_func,
        'seg': paint_segments,
        'hot': paint_hot,
        'gau': paint_gaussian,
        'ggau': paint_generalized_gaussian,
    }[chosen]
    paint(save_pdf)


def plot_curves():
    import json
    plt.figure(num='result', figsize=(8.5, 6))
    
    def get_li(fname):
        path = '/Users/tiankeyu/Downloads/avgacc'
        path = os.path.join(path, fname + '.json')
        li = []
        with open(path, 'r') as f:
            li = json.load(f)
        li = [x[2] for x in li]
        vv = li[0]
        ml = [vv]
        gm = 0.86
        for i in range(len(li)):
            if i > 0:
                vv = vv*gm + li[i] * (1-gm)
                ml.append(vv)
        li = ml
        
        li = np.array(li)
        li = - li[:50].mean() + li + 96.585
        
        print(f'len({fname}) == {len(li)}')
        return li
    
    best_li = get_li('best')
    alr1_li = get_li('alr0.5')
    alr001_li = get_li('alr0.05')
    q8_li = get_li('freq8')
    q128_li = get_li('freq128')
    
    ll = min([len(best_li), len(alr1_li), len(alr001_li), len(q8_li), len(q128_li)])
    best_li = best_li[:ll]
    alr1_li = alr1_li[:ll]
    alr001_li = alr001_li[:ll]
    q8_li = q8_li[:ll]
    q128_li = q128_li[:ll]

    plt.plot(list(range(ll)), best_li, label='$\\eta_\\theta=0.1$, $N_b=32$', c='steelblue')
    plt.plot(list(range(ll)), alr001_li, label='$\\eta_\\theta=0.01$, $N_b=32$', c='tomato')
    plt.plot(list(range(ll)), alr1_li, label='$\\eta_\\theta=1$, $N_b=32$', c='darkviolet')
    # plt.plot(list(range(ll)), q8_li, label='$\\eta_\\theta=0.1$, $N_b=8$', c='tomato')
    # plt.plot(list(range(ll)), q128_li, label='$\\eta_\\theta=0.1$, $N_b=128$', c='darkviolet')
    
    plt.xlabel('one-shot search times', labelpad=25)
    plt.ylabel(r'moving average of ACC$(\bar{\omega}_{\theta}^*)$', labelpad=32)
    plt.legend(loc='upper left')
    
    render(False, 'Sensitivity to $\\eta_\\theta$')


if __name__ == '__main__':
    LEGEND_FONT_SIZE = 22
    GENERAL_FONT_SIZE = 25
    plt.rcParams.update({
        # 'figure.dpi': 200,  # 300 => 1800*1200, 200 => 1200*800
        # 'savefig.dpi': 200,  # 300 => 1800*1200, 200 => 1200*800
        'figure.figsize': (7.2, 4.8),
        'font.size': LEGEND_FONT_SIZE,              # legend title
        'legend.fontsize': LEGEND_FONT_SIZE,        # legend label
        'axes.titlesize': GENERAL_FONT_SIZE,        # fig title
        'axes.labelsize': GENERAL_FONT_SIZE + 2,        # axes label
        'xtick.labelsize': GENERAL_FONT_SIZE,       # xtick label
        'ytick.labelsize': GENERAL_FONT_SIZE,       # ytick label
        # 'figure.titlesize': GENERAL_FONT_SIZE,    # unknown
    })
    # main()
    plot_curves()

"""
's' : 方块状
'o' : 实心圆
'^' : 正三角形
'v' : 反正三角形
'+' : 加号
'*' : 星号
'x' : x号
'p' : 五角星
'1' : 三脚架标记
'2' : 三脚架标记
'$❤$' : 爱心
"""
