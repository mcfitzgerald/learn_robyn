import plotly.graph_objects as go
import plotly.io as pio

pio.templates["mike"] = go.layout.Template(
    {
        "data": {
            "histogram2dcontour": [
                {
                    "type": "histogram2dcontour",
                    "colorbar": {
                        "outlinewidth": 1,
                        "tickcolor": "rgb(36,36,36)",
                        "ticks": "outside",
                    },
                    "colorscale": [
                        [0.0, "#440154"],
                        [0.1111111111111111, "#482878"],
                        [0.2222222222222222, "#3e4989"],
                        [0.3333333333333333, "#31688e"],
                        [0.4444444444444444, "#26828e"],
                        [0.5555555555555556, "#1f9e89"],
                        [0.6666666666666666, "#35b779"],
                        [0.7777777777777778, "#6ece58"],
                        [0.8888888888888888, "#b5de2b"],
                        [1.0, "#fde725"],
                    ],
                }
            ],
            "choropleth": [
                {
                    "type": "choropleth",
                    "colorbar": {
                        "outlinewidth": 1,
                        "tickcolor": "rgb(36,36,36)",
                        "ticks": "outside",
                    },
                }
            ],
            "histogram2d": [
                {
                    "type": "histogram2d",
                    "colorbar": {
                        "outlinewidth": 1,
                        "tickcolor": "rgb(36,36,36)",
                        "ticks": "outside",
                    },
                    "colorscale": [
                        [0.0, "#440154"],
                        [0.1111111111111111, "#482878"],
                        [0.2222222222222222, "#3e4989"],
                        [0.3333333333333333, "#31688e"],
                        [0.4444444444444444, "#26828e"],
                        [0.5555555555555556, "#1f9e89"],
                        [0.6666666666666666, "#35b779"],
                        [0.7777777777777778, "#6ece58"],
                        [0.8888888888888888, "#b5de2b"],
                        [1.0, "#fde725"],
                    ],
                }
            ],
            "heatmap": [
                {
                    "type": "heatmap",
                    "colorbar": {
                        "outlinewidth": 1,
                        "tickcolor": "rgb(36,36,36)",
                        "ticks": "outside",
                    },
                    "colorscale": [
                        [0.0, "#440154"],
                        [0.1111111111111111, "#482878"],
                        [0.2222222222222222, "#3e4989"],
                        [0.3333333333333333, "#31688e"],
                        [0.4444444444444444, "#26828e"],
                        [0.5555555555555556, "#1f9e89"],
                        [0.6666666666666666, "#35b779"],
                        [0.7777777777777778, "#6ece58"],
                        [0.8888888888888888, "#b5de2b"],
                        [1.0, "#fde725"],
                    ],
                }
            ],
            "heatmapgl": [
                {
                    "type": "heatmapgl",
                    "colorbar": {
                        "outlinewidth": 1,
                        "tickcolor": "rgb(36,36,36)",
                        "ticks": "outside",
                    },
                    "colorscale": [
                        [0.0, "#440154"],
                        [0.1111111111111111, "#482878"],
                        [0.2222222222222222, "#3e4989"],
                        [0.3333333333333333, "#31688e"],
                        [0.4444444444444444, "#26828e"],
                        [0.5555555555555556, "#1f9e89"],
                        [0.6666666666666666, "#35b779"],
                        [0.7777777777777778, "#6ece58"],
                        [0.8888888888888888, "#b5de2b"],
                        [1.0, "#fde725"],
                    ],
                }
            ],
            "contourcarpet": [
                {
                    "type": "contourcarpet",
                    "colorbar": {
                        "outlinewidth": 1,
                        "tickcolor": "rgb(36,36,36)",
                        "ticks": "outside",
                    },
                }
            ],
            "contour": [
                {
                    "type": "contour",
                    "colorbar": {
                        "outlinewidth": 1,
                        "tickcolor": "rgb(36,36,36)",
                        "ticks": "outside",
                    },
                    "colorscale": [
                        [0.0, "#440154"],
                        [0.1111111111111111, "#482878"],
                        [0.2222222222222222, "#3e4989"],
                        [0.3333333333333333, "#31688e"],
                        [0.4444444444444444, "#26828e"],
                        [0.5555555555555556, "#1f9e89"],
                        [0.6666666666666666, "#35b779"],
                        [0.7777777777777778, "#6ece58"],
                        [0.8888888888888888, "#b5de2b"],
                        [1.0, "#fde725"],
                    ],
                }
            ],
            "surface": [
                {
                    "type": "surface",
                    "colorbar": {
                        "outlinewidth": 1,
                        "tickcolor": "rgb(36,36,36)",
                        "ticks": "outside",
                    },
                    "colorscale": [
                        [0.0, "#440154"],
                        [0.1111111111111111, "#482878"],
                        [0.2222222222222222, "#3e4989"],
                        [0.3333333333333333, "#31688e"],
                        [0.4444444444444444, "#26828e"],
                        [0.5555555555555556, "#1f9e89"],
                        [0.6666666666666666, "#35b779"],
                        [0.7777777777777778, "#6ece58"],
                        [0.8888888888888888, "#b5de2b"],
                        [1.0, "#fde725"],
                    ],
                }
            ],
            "mesh3d": [
                {
                    "type": "mesh3d",
                    "colorbar": {
                        "outlinewidth": 1,
                        "tickcolor": "rgb(36,36,36)",
                        "ticks": "outside",
                    },
                }
            ],
            "scatter": [
                {
                    "fillpattern": {"fillmode": "overlay", "size": 10, "solidity": 0.2},
                    "type": "scatter",
                }
            ],
            "parcoords": [
                {
                    "type": "parcoords",
                    "line": {
                        "colorbar": {
                            "outlinewidth": 1,
                            "tickcolor": "rgb(36,36,36)",
                            "ticks": "outside",
                        }
                    },
                }
            ],
            "scatterpolargl": [
                {
                    "type": "scatterpolargl",
                    "marker": {
                        "colorbar": {
                            "outlinewidth": 1,
                            "tickcolor": "rgb(36,36,36)",
                            "ticks": "outside",
                        }
                    },
                }
            ],
            "bar": [
                {
                    "error_x": {"color": "rgb(36,36,36)"},
                    "error_y": {"color": "rgb(36,36,36)"},
                    "marker": {
                        "line": {"color": "white", "width": 0.5},
                        "pattern": {"fillmode": "overlay", "size": 10, "solidity": 0.2},
                    },
                    "type": "bar",
                }
            ],
            "scattergeo": [
                {
                    "type": "scattergeo",
                    "marker": {
                        "colorbar": {
                            "outlinewidth": 1,
                            "tickcolor": "rgb(36,36,36)",
                            "ticks": "outside",
                        }
                    },
                }
            ],
            "scatterpolar": [
                {
                    "type": "scatterpolar",
                    "marker": {
                        "colorbar": {
                            "outlinewidth": 1,
                            "tickcolor": "rgb(36,36,36)",
                            "ticks": "outside",
                        }
                    },
                }
            ],
            "histogram": [
                {
                    "marker": {"line": {"color": "white", "width": 0.6}},
                    "type": "histogram",
                }
            ],
            "scattergl": [
                {
                    "type": "scattergl",
                    "marker": {
                        "colorbar": {
                            "outlinewidth": 1,
                            "tickcolor": "rgb(36,36,36)",
                            "ticks": "outside",
                        }
                    },
                }
            ],
            "scatter3d": [
                {
                    "type": "scatter3d",
                    "line": {
                        "colorbar": {
                            "outlinewidth": 1,
                            "tickcolor": "rgb(36,36,36)",
                            "ticks": "outside",
                        }
                    },
                    "marker": {
                        "colorbar": {
                            "outlinewidth": 1,
                            "tickcolor": "rgb(36,36,36)",
                            "ticks": "outside",
                        }
                    },
                }
            ],
            "scattermapbox": [
                {
                    "type": "scattermapbox",
                    "marker": {
                        "colorbar": {
                            "outlinewidth": 1,
                            "tickcolor": "rgb(36,36,36)",
                            "ticks": "outside",
                        }
                    },
                }
            ],
            "scatterternary": [
                {
                    "type": "scatterternary",
                    "marker": {
                        "colorbar": {
                            "outlinewidth": 1,
                            "tickcolor": "rgb(36,36,36)",
                            "ticks": "outside",
                        }
                    },
                }
            ],
            "scattercarpet": [
                {
                    "type": "scattercarpet",
                    "marker": {
                        "colorbar": {
                            "outlinewidth": 1,
                            "tickcolor": "rgb(36,36,36)",
                            "ticks": "outside",
                        }
                    },
                }
            ],
            "carpet": [
                {
                    "aaxis": {
                        "endlinecolor": "rgb(36,36,36)",
                        "gridcolor": "white",
                        "linecolor": "white",
                        "minorgridcolor": "white",
                        "startlinecolor": "rgb(36,36,36)",
                    },
                    "baxis": {
                        "endlinecolor": "rgb(36,36,36)",
                        "gridcolor": "white",
                        "linecolor": "white",
                        "minorgridcolor": "white",
                        "startlinecolor": "rgb(36,36,36)",
                    },
                    "type": "carpet",
                }
            ],
            "table": [
                {
                    "cells": {
                        "fill": {"color": "rgb(237,237,237)"},
                        "line": {"color": "white"},
                    },
                    "header": {
                        "fill": {"color": "rgb(217,217,217)"},
                        "line": {"color": "white"},
                    },
                    "type": "table",
                }
            ],
            "barpolar": [
                {
                    "marker": {
                        "line": {"color": "white", "width": 0.5},
                        "pattern": {"fillmode": "overlay", "size": 10, "solidity": 0.2},
                    },
                    "type": "barpolar",
                }
            ],
            "pie": [{"automargin": True, "type": "pie"}],
        },
        "layout": {
            "autotypenumbers": "strict",
            "colorway": [
                "rgb(190, 190, 190)",
                "rgb(167, 167, 167)",
                "rgb(144, 144, 144)",
                "rgb(122, 122, 122)",
                "rgb(101, 101, 101)",
                "rgb(80, 80, 80)",
                "rgb(61, 61, 61)",
                "rgb(42, 42, 42)",
                "rgb(25, 25, 25)",
                "rgb(0, 0, 0)",
            ],
            "font": {"color": "rgb(36,36,36)", "family": "Helvetica"},
            "hovermode": "closest",
            "hoverlabel": {"align": "left"},
            "paper_bgcolor": "white",
            "plot_bgcolor": "white",
            "polar": {
                "bgcolor": "white",
                "angularaxis": {
                    "gridcolor": "rgb(232,232,232)",
                    "linecolor": "rgb(36,36,36)",
                    "showgrid": False,
                    "showline": True,
                    "ticks": "outside",
                },
                "radialaxis": {
                    "gridcolor": "rgb(232,232,232)",
                    "linecolor": "rgb(36,36,36)",
                    "showgrid": False,
                    "showline": True,
                    "ticks": "outside",
                },
            },
            "ternary": {
                "bgcolor": "white",
                "aaxis": {
                    "gridcolor": "rgb(232,232,232)",
                    "linecolor": "rgb(36,36,36)",
                    "showgrid": False,
                    "showline": True,
                    "ticks": "outside",
                },
                "baxis": {
                    "gridcolor": "rgb(232,232,232)",
                    "linecolor": "rgb(36,36,36)",
                    "showgrid": False,
                    "showline": True,
                    "ticks": "outside",
                },
                "caxis": {
                    "gridcolor": "rgb(232,232,232)",
                    "linecolor": "rgb(36,36,36)",
                    "showgrid": False,
                    "showline": True,
                    "ticks": "outside",
                },
            },
            "coloraxis": {
                "colorbar": {
                    "outlinewidth": 1,
                    "tickcolor": "rgb(36,36,36)",
                    "ticks": "outside",
                }
            },
            "colorscale": {
                "sequential": [
                    [0.0, "rgb(255,255,255)"],
                    [0.125, "rgb(240,240,240)"],
                    [0.25, "rgb(217,217,217)"],
                    [0.375, "rgb(189,189,189)"],
                    [0.5, "rgb(150,150,150)"],
                    [0.625, "rgb(115,115,115)"],
                    [0.75, "rgb(82,82,82)"],
                    [0.875, "rgb(37,37,37)"],
                    [1.0, "rgb(0,0,0)"],
                ],
                "sequentialminus": [
                    [0.0, "#440154"],
                    [0.1111111111111111, "#482878"],
                    [0.2222222222222222, "#3e4989"],
                    [0.3333333333333333, "#31688e"],
                    [0.4444444444444444, "#26828e"],
                    [0.5555555555555556, "#1f9e89"],
                    [0.6666666666666666, "#35b779"],
                    [0.7777777777777778, "#6ece58"],
                    [0.8888888888888888, "#b5de2b"],
                    [1.0, "#fde725"],
                ],
                "diverging": [
                    [0.0, "rgb(103,0,31)"],
                    [0.1, "rgb(178,24,43)"],
                    [0.2, "rgb(214,96,77)"],
                    [0.3, "rgb(244,165,130)"],
                    [0.4, "rgb(253,219,199)"],
                    [0.5, "rgb(247,247,247)"],
                    [0.6, "rgb(209,229,240)"],
                    [0.7, "rgb(146,197,222)"],
                    [0.8, "rgb(67,147,195)"],
                    [0.9, "rgb(33,102,172)"],
                    [1.0, "rgb(5,48,97)"],
                ],
            },
            "xaxis": {
                "gridcolor": "rgb(232,232,232)",
                "linecolor": "rgb(36,36,36)",
                "showgrid": False,
                "showline": True,
                "ticks": "outside",
                "title": {"standoff": 15},
                "zerolinecolor": "rgb(36,36,36)",
                "automargin": True,
                "zeroline": False,
                "mirror": True,
            },
            "yaxis": {
                "gridcolor": "rgb(232,232,232)",
                "linecolor": "rgb(36,36,36)",
                "showgrid": False,
                "showline": True,
                "ticks": "outside",
                "title": {"standoff": 15},
                "zerolinecolor": "rgb(36,36,36)",
                "automargin": True,
                "zeroline": False,
                "mirror": True,
            },
            "scene": {
                "xaxis": {
                    "backgroundcolor": "white",
                    "gridcolor": "rgb(232,232,232)",
                    "linecolor": "rgb(36,36,36)",
                    "showbackground": True,
                    "showgrid": False,
                    "showline": True,
                    "ticks": "outside",
                    "zerolinecolor": "rgb(36,36,36)",
                    "gridwidth": 2,
                    "zeroline": False,
                },
                "yaxis": {
                    "backgroundcolor": "white",
                    "gridcolor": "rgb(232,232,232)",
                    "linecolor": "rgb(36,36,36)",
                    "showbackground": True,
                    "showgrid": False,
                    "showline": True,
                    "ticks": "outside",
                    "zerolinecolor": "rgb(36,36,36)",
                    "gridwidth": 2,
                    "zeroline": False,
                },
                "zaxis": {
                    "backgroundcolor": "white",
                    "gridcolor": "rgb(232,232,232)",
                    "linecolor": "rgb(36,36,36)",
                    "showbackground": True,
                    "showgrid": False,
                    "showline": True,
                    "ticks": "outside",
                    "zerolinecolor": "rgb(36,36,36)",
                    "gridwidth": 2,
                    "zeroline": False,
                },
            },
            "shapedefaults": {
                "fillcolor": "black",
                "line": {"width": 0},
                "opacity": 0.3,
            },
            "annotationdefaults": {"arrowhead": 0, "arrowwidth": 1},
            "geo": {
                "bgcolor": "white",
                "landcolor": "white",
                "subunitcolor": "white",
                "showland": True,
                "showlakes": True,
                "lakecolor": "white",
            },
            "title": {"x": 0.05},
            "mapbox": {"style": "light"},
        },
    }
)