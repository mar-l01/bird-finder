def compute_iou(bb_target: tuple, bb_pred: tuple) -> float:
    """
    Compute the intersection over union metric of two bounding boxes:
    - bb_target: the target bounding box
    - bb_pred: the predicted bounding box
    """
    xt_s, yt_s, xt_e, yt_e = bb_target
    xp_s, yp_s, xp_e, yp_e = bb_pred

    # intersection rectangle coordinates
    xi_s = max(xt_s, xp_s)
    yi_s = max(yt_s, yp_s)
    xi_e = min(xt_e, xp_e)
    yi_e = min(yt_e, yp_e)

    # no overlapping at all
    if xi_e < xi_s or yi_e < yi_s:
        return 0.0

    # area intersection rectangle
    a_i = abs(xi_e - xi_s) * abs(yi_e - yi_s)

    # area of both rectangles
    a_t = abs(xt_e - xt_s) * abs(yt_e - yt_s)
    a_p = abs(xp_e - xp_s) * abs(yp_e - yp_s)
    a_u = a_t + a_p - a_i

    return a_i / a_u


def label_iou(iou: float) -> str:
    """
    Label a computed intersection over union value according to below mapping.
    """
    if iou == 1:
        return "excellent"
    elif iou > .9:
        return "perfect"
    elif iou > .8:
        return "very good"
    elif iou > .7:
        return "good"
    elif iou > .5:
        return "acceptable"

    return "poor"
