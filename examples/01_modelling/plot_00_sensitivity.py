#!/usr/bin/env python
# *-* coding: utf-8 *-*
"""
Plotting sensitivities
^^^^^^^^^^^^^^^^^^^^^^

Sensitivity distributions can be easily plotted using the tdMan class:
"""
###############################################################################
# imports
import numpy as np
import crtomo
# is only used for reda.CreateEnterDirectory
import reda

###############################################################################
# create and save a FEM-grid
grid = crtomo.crt_grid.create_surface_grid(
    nr_electrodes=10,
    spacing=1,
    depth=4,
    char_lengths=0.2,
)

grid.plot_grid()

with reda.CreateEnterDirectory('output_plot_00_sensitivity'):
    grid.save_elem_file('elem.dat')
    grid.save_elec_file('elec.dat')

###############################################################################
# create the measurement configuration
configs = np.array((
    (1, 4, 10, 7),
))


###############################################################################
# for different background, plot the sensitivities
for bg in (1, 10, 100, 1000):
    td = crtomo.tdMan(grid=grid)
    td.configs.add_to_configs(configs)
    td.add_homogeneous_model(bg, 0)

    td.model(sensitivities=True, silent=True)
    r = td.plot_sensitivity(0)
    with reda.CreateEnterDirectory('output_plot_00_sensitivity'):
        r[0].savefig('sensitivity_bg_{}.pdf'.format(bg), bbox_inches='tight')
    r = td.plot_sensitivity(0, mag_only=True)
    with reda.CreateEnterDirectory('output_plot_00_sensitivity'):
        r[0].savefig(
            'sensitivity_magonly_bg_{}.pdf'.format(bg), bbox_inches='tight')
