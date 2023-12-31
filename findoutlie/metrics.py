""" Scan outlier metrics
"""

# Any imports you need
import numpy as np
import nipraxis

# +++your code here+++


def dvars(img):
    """ Calculate dvars metric on Nibabel image `img`

    The dvars calculation between two volumes is defined as the square root of
    (the mean of the (voxel differences squared)).

    Parameters
    ----------
    img : nibabel image

    Returns
    -------
    dvals : 1D array
        One-dimensional array with n-1 elements, where n is the number of
        volumes in `img`.
    """
    # Hint: remember 'axis='.  For example:
    # In [2]: arr = np.array([[2, 3, 4], [5, 6, 7]])
    # In [3]: np.mean(arr, axis=1)
    # Out[2]: array([3., 6.])
    #

    data = img.get_fdata()
    dvals = []
    for i in range(1, data.shape[-1]):
        # this_vol = data[..., i]
        # prev_vol = data[..., (i-1)]
        vol_diff = data[..., i] - data[..., (i-1)]
        dvar_val = np.sqrt(np.mean(vol_diff ** 2))
        dvals.append(dvar_val)
    return np.array(dvals)
