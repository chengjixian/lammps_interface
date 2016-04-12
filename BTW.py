#### BTW-FF atom types and properties #####
BTW_atoms = {
#FF_num  at_num  at_mass   valance vdW_rad[A]  epsilo[kcal/mol] H-bond  charge   atom_type  description
"170":(  8       ,15.9994  ,2.0    ,1.82       ,0.059           ,0      ,-1.181 ),#  O       O-Carboxylate                                
"902":(  6       ,12       ,3.0    ,1.96       ,0.056           ,0      , -0.056),#  C       Calpha
"913":(  6       ,12       ,3.0    ,1.94       ,0.056           ,0      , 1.576 ),#  C       Cacid
"912":(  6       ,12       ,3.0    ,1.96       ,0.056           ,0      ,-0.058 ),#  C       Cbenzene
"915":(  1       ,1.008    ,1.0    ,1.62       ,0.02            ,0.923  , 0.129 ),#  H       Hbenzene                        
"75" :(  8       ,15.9994  ,4.0    ,1.82       ,0.059           ,0      ,-1.242 ),#  O       O-H
"192":(  40      ,91.224   ,8.0    ,3.52       ,0.367           ,0      , 2.601 ),#  Zr      Zr
"21" :(  1       ,1.008    ,1.0    ,1.62       ,0.02            ,0.923  , 0.622 ),#  H       H-Oi                            
"171":(  8       ,15.9994  ,4.0    ,1.82       ,0.059           ,0      ,-1.189 ),#  O       O-inorganic
"903":(  6       ,12       ,3.0    ,1.96       ,0.056           ,0      ,-0.035 ) #  C       C-doublephenolligand            }
}

####   BONDs in BTW-FF ####
BTW_bonds = {
#FF_bond    k [kcal/mol/A^2]	r [A]
"21_75"  :( 3.630,   0.989),
"75_192" :( 5.500,   2.276),
"171_192":( 5.809,   2.192),
"192_170":( 5.821,   2.338),
"912_915":( 5.150,   1.101), 
"913_170":( 5.999,   1.299), 
"913_902":( 5.299,   1.485), 
"912_912":( 4.500,   1.389), 
"902_912":( 4.500,   1.389), 
"903_903":( 5.899,   1.465),
"903_912":( 5.999,   1.389),
"913_170":( 5.999,   1.299),
}
#### ANGLES in BTW-FF ####
BTW_angles = {
# at1_atcen_at2     k[kcal/mol] Theta[degree]
"170_913_170":(     2.867,      126.299,    0.0  ,   0.0  ,   0.0  ,  0.0 , 0.0 ), 
"902_913_170":(     1.867,      117.082,    0.0  ,   0.0  ,   0.0  ,  0.0 , 0.0 ),     
"912_902_912":(     0.000,      119.406,    0.0  ,   0.0  ,   0.0  ,  0.0 , 0.0 ),
"902_912_912":(     0.060,      121.582,    0.0  ,   0.0  ,   0.0  ,  0.0 , 0.0 ),
"912_902_913":(     0.360,      121.797,    0.0  ,   0.0  ,   0.0  ,  0.0 , 0.0 ),
"902_912_915":(     0.090,      119.859,    0.0  ,   0.0  ,   0.0  ,  0.0 , 0.0 ),
"903_903_912":(     5.00 ,      122.690,    0.0  ,   0.0  ,   0.0  ,  0.0 , 0.0 ),
"912_903_912":(     5.00 ,      117.621,    0.0  ,   0.0  ,   0.0  ,  0.0 , 0.0 ),
"903_912_912":(     5.00 ,      122.904,    0.0  ,   0.0  ,   0.0  ,  0.0 , 0.0 ),
"903_912_915":(     5.00 ,      120.00 ,    0.0  ,   0.0  ,   0.0  ,  0.0 , 0.0 ),
"171_192_170":(     2.099,      84.318 ,    0.0  ,   0.0  ,   0.0  ,  0.0 , 0.0 ),
"192_170_913":(     2.099,      139.820,    0.0  ,   0.0  ,   0.0  ,  0.0 , 0.0 ),
"170_192_170":(     2.099,      73.103 ,    0.0  ,   0.0  ,   0.0  ,  0.0 , 0.0 ),
"192_171_192":(     2.099,      118.053,    0.0  ,   0.0  ,   0.0  ,  0.0 , 0.0 ),
"21_75_192"  :(     2.099,      116.848,    0.0  ,   0.0  ,   0.0  ,  0.0 , 0.0 ),
"192_75_192" :(     2.099,      103.406,    0.0  ,   0.0  ,   0.0  ,  0.0 , 0.0 ),
"192_171_192":(     2.099,      118.408,    0.0  ,   0.0  ,   0.0  ,  0.0 , 0.0 ),
"170_192_75" :(     2.099,      89.658 ,    0.0  ,   0.0  ,   0.0  ,  0.0 , 0.0 ),
"171_192_75" :(     2.099,      71.110 ,    0.0  ,   0.0  ,   0.0  ,  0.0 , 0.0 ),
"192_75_192" :(     2.099,      103.406,    0.0  ,   0.0  ,   0.0  ,  0.0 , 0.0 ),
"75_192_75"  :(     2.099,      123.230,    0.0  ,   0.0  ,   0.0  ,  0.0 , 0.0 ),
"75_192_171" :(     2.099,      71.110 ,    0.0  ,   0.0  ,   0.0  ,  0.0 , 0.0 ),
"171_192_171":(     2.099,      91.479 ,    0.0  ,   0.0  ,   0.0  ,  0.0 , 0.0 ), 
"912_903_903":(     5.00 ,      122.690,    0.0  ,   0.0  ,   0.0  ,  0.0 , 0.0 ),
"912_903_912":(     5.00 ,      117.621,    0.0  ,   0.0  ,   0.0  ,  0.0 , 0.0 ),
"912_912_903":(     5.00 ,      122.904,    0.0  ,   0.0  ,   0.0  ,  0.0 , 0.0 ),
"915_912_903":(     5.00 ,      120.00 ,    0.0  ,   0.0  ,   0.0  ,  0.0 , 0.0 ),
"912_912_915":(     0.49 ,      120.0  ,    0.08 ,   0.0  ,   0.0  ,  0.0 , 0.0 )  #    added from MM3 
}
#### DIHEDRALs in BTW-FF
BTW_dihedrals = {
# atom1_atom2_atom3_atom4 k_1[kcal/mol/rad^2] thetha1[degree] n1 k_2[kcal/mol/rad^2] thetha2[degree] n2 k_3[kcal/mol/rad^2] thetha3[degree] n3
"170_913_902_912":(    0.0 , 0.0 , 1 , 2.5   , 180.0 , 2 ,  0.0 , 0.0 , 3 , 0.0 , 0.0 , 4), 
"915_912_902_913":(    0.0 , 0.0 , 1 , 1.999 , 180.0 , 2 ,  0.0 , 0.0 , 3 , 0.0 , 0.0 , 4),
"913_902_912_912":(    0.0 , 0.0 , 1 , 8.030 , 180.0 , 2 ,  0.0 , 0.0 , 3 , 0.0 , 0.0 , 4),
"912_902_912_912":(    0.0 , 0.0 , 1 , 8.030 , 180.0 , 2 ,  0.0 , 0.0 , 3 , 0.0 , 0.0 , 4),
"912_902_912_915":(    0.0 , 0.0 , 1 , 8.030 , 180.0 , 2 ,  0.0 , 0.0 , 3 , 0.0 , 0.0 , 4),
"902_912_912_915":(    0.0 , 0.0 , 1 , 8.030 , 180.0 , 2 ,  0.0 , 0.0 , 3 , 0.0 , 0.0 , 4),
"902_912_912_902":(    0.0 , 0.0 , 1 , 8.030 , 180.0 , 2 ,  0.0 , 0.0 , 3 , 0.0 , 0.0 , 4),
"903_903_912_915":(    0.0 , 0.0 , 1 , 6.999 , 180.0 , 2 ,  0.0 , 0.0 , 3 , 0.0 , 0.0 , 4),
"903_903_912_912":(    0.0 , 0.0 , 1 , 6.9   , 180.0 , 2 ,  0.0 , 0.0 , 3 , 0.0 , 0.0 , 4),
"912_903_903_912":(    0.0 , 0.0 , 1 , 6.9   , 180.0 , 2 ,  0.0 , 0.0 , 3 , 0.0 , 0.0 , 4),
"912_903_912_912":(    0.0 , 0.0 , 1 , 4.930 , 180.0 , 2 ,  0.0 , 0.0 , 3 , 0.0 , 0.0 , 4),
"912_903_912_915":(    0.0 , 0.0 , 1 , 4.930 , 180.0 , 2 ,  0.0 , 0.0 , 3 , 0.0 , 0.0 , 4),
"915_912_912_903":(    0.0 , 0.0 , 1 , 4.930 , 180.0 , 2 ,  0.0 , 0.0 , 3 , 0.0 , 0.0 , 4),
"902_912_912_903":(    0.0 , 0.0 , 1 , 5.930 , 180.0 , 2 ,  0.0 , 0.0 , 3 , 0.0 , 0.0 , 4),
"902_912_912_912":(    0.0 , 0.0 , 1 , 8.030 , 180.0 , 2 ,  0.0 , 0.0 , 3 , 0.0 , 0.0 , 4),
"171_192_170_913":(    0.0 , 0.0 , 1 , 2.064 , 180.0 , 2 ,  0.0 , 0.0 , 3 , 0.0 , 0.0 , 4),
"192_170_913_170":(    0.0 , 0.0 , 1 , 2.017 , 180.0 , 2 ,  0.0 , 0.0 , 3 , 0.0 , 0.0 , 4),
"915_912_902_913":(    0.0 , 0.0 , 1 , 1.999 , 180.0 , 2 ,  0.0 , 0.0 , 3 , 0.0 , 0.0 , 4),
"170_192_170_913":(    0.0 , 0.0 , 1 , 0.860 , 180.0 , 2 ,  0.0 , 0.0 , 3 , 0.0 , 0.0 , 4),
"192_170_913_902":(    0.0 , 0.0 , 1 , 0.072 , 180.0 , 2 ,  0.0 , 0.0 , 3 , 0.0 , 0.0 , 4),
"170_192_171_192":(    0.0 , 0.0 , 1 , 1.000 , 180.0 , 2 ,  0.0 , 0.0 , 3 , 0.0 , 0.0 , 4),
"913_170_192_75" :(    0.0 , 0.0 , 1 , 5.000 , 180.0 , 2 ,  0.0 , 0.0 , 3 , 0.0 , 0.0 , 4),
"21_75_192_170"  :(    0.0 , 0.0 , 1 , 5.000 , 180.0 , 2 ,  0.0 , 0.0 , 3 , 0.0 , 0.0 , 4),
"21_75_191_170"  :(    0.0 , 0.0 , 1 , 5.000 , 180.0 , 2 ,  0.0 , 0.0 , 3 , 0.0 , 0.0 , 4),
"192_75_192_170" :(    0.0 , 0.0 , 1 , 5.000 , 180.0 , 2 ,  0.0 , 0.0 , 3 , 0.0 , 0.0 , 4),
"192_75_192_75"  :(    0.0 , 0.0 , 1 , 5.000 , 180.0 , 2 ,  0.0 , 0.0 , 3 , 0.0 , 0.0 , 4),
"192_75_192_171" :(    0.0 , 0.0 , 1 , 5.000 , 180.0 , 2 ,  0.0 , 0.0 , 3 , 0.0 , 0.0 , 4),
"21_75_192_75"   :(    0.0 , 0.0 , 1 , 5.000 , 180.0 , 2 ,  0.0 , 0.0 , 3 , 0.0 , 0.0 , 4),
"192_75_192_171" :(    0.0 , 0.0 , 1 , 5.000 , 180.0 , 2 ,  0.0 , 0.0 , 3 , 0.0 , 0.0 , 4),
"192_171_192_75" :(    0.0 , 0.0 , 1 , 5.000 , 180.0 , 2 ,  0.0 , 0.0 , 3 , 0.0 , 0.0 , 4),
"192_171_192_171":(    0.0 , 0.0 , 1 , 5.000 , 180.0 , 2 ,  0.0 , 0.0 , 3 , 0.0 , 0.0 , 4),
"21_75_192_171"  :(    0.0 , 0.0 , 1 , 5.000 , 180.0 , 2 ,  0.0 , 0.0 , 3 , 0.0 , 0.0 , 4),
"192_75_192_171" :(    0.0 , 0.0 , 1 , 5.000 , 180.0 , 2 ,  0.0 , 0.0 , 3 , 0.0 , 0.0 , 4),
"192_171_192_75" :(    0.0 , 0.0 , 1 , 5.000 , 180.0 , 2 ,  0.0 , 0.0 , 3 , 0.0 , 0.0 , 4),
"915_912_912_915":(    0.0 , 0.0 , 1 , 11.5  , 180.0 , 2 ,  0.0 , 0.0 , 3 , 0.0 , 0.0 , 4)  # added from MM3

}
#### Out-of-Plane bending in BTW-FF
BTW_opbends = {
# atom1_atom2_atom3_atom4 K[kcal/mol/rad^2] theta[degree]
#"170_913_170_902":(	1.5, 180.0 ),     # these two should be enumarated to cover all possible set 
###    """
###          H
###         /
###    C = C 
###         \
###          C
###    """
"902_912_912_915":( 0.0 , 0.0  ,  0.24  , 0.300  ,  0.0    ),# BTW = 0.0 while is equal to 0.2 in MM3 
"902_912_915_912":( 0.0 , 0.0  ,  0.24  , 0.300  ,  0.0    ),# BTW = 0.0 while is equal to 0.2 in MM3 
"912_912_902_915":( 0.2 , 0.0  ,  0.24  , 0.300  ,  0.0    ),# Added from MM3 to complete the missing parameters. Also it was in BTW unintentionally
"912_912_915_902":( 0.2 , 0.0  ,  0.24  , 0.300  ,  0.0    ),# Added from MM3 to complete the missing parameters. Also it was in BTW unintentionall 
"915_912_902_912":( 0.11, 0.0  ,  0.24  , 0.300  ,  0.0    ),# Added from MM3 to complete the missing parameters. Also it was in BTW unintentionall 
"915_912_912_902":( 0.11, 0.0  ,  0.24  , 0.300  ,  0.0    ),# Added from MM3 to complete the missing parameters. Also it was in BTW unintentionall 
###   """
###         O
###        /
###   C = C
###        \
###         O
###   """
"170_913_170_902":(1.5 , 0.0 ,  0.24  , 0.300  ,  0.0    ),# Added from BTW-FF 
"170_913_902_170":(1.5 , 0.0 ,  0.24  , 0.300  ,  0.0    ),# Added from BTW-FF 
"902_913_170_170":(0.0 , 0.0 ,  0.24  , 0.300  ,  0.0    ),# BTW = 0.0 while is equal to 0.8 in MM3 
###   """
###         C
###        /
###   C = C
###        \
###         C 
###   """
"912_902_912_913":( 0.2, 0.0 ,  0.24  , 0.300  ,  0.0   ),# Added from MM3 to complete the missing parameters. Alsi it was in BTW-FF unintentionally
"912_902_913_912":( 0.2, 0.0 ,  0.24  , 0.300  ,  0.0   ),# Added from MM3 to complete the missing parameters. Alsi it was in BTW-FF unintentionall#
"913_902_912_912":( 0.8, 0.0 ,  0.24  , 0.300  ,  0.0   ),# Added from MM3 to complete the missing parameters. Alsi it was in BTW-FF unintentionall# 
#
# UIO special opbend
#
"192_171_192_192":( 2.0 , 0.0 ,  0.24  , 0.300  ,  0.0   ),# Added from MM3 to complete the missing parameters. Alsi it was in BTW-FF unintentionall# 
}

