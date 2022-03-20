units		metal
variable cfac equal 1.0e-4
variable cunits string GPa

variable etol equal 0.0 
variable ftol equal 1.0e-10
variable maxiter equal 100
variable maxeval equal 1000
variable dmax equal 1.0e-2

atom_style	atomic
boundary        p p p
box tilt large

read_data        input.pos

mass 1 28.0855
mass 2 15.9994

