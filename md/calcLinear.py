import sys
import getfem as gf
import numpy as np

def main(mesh_file, output_name):
    degree = 2
    E = 1e3
    Nu = 0.3
    Lambda = E*Nu / ((1+Nu)*(1-2*Nu))
    Mu = E/(2*(1+Nu))

    m = gf.Mesh('import', 'gmsh', mesh_file)
    
    mfu = gf.MeshFem(m,3)
    mfp = gf.MeshFem(m,1)

    mfu.set_fem(gf.Fem('FEM_PK(3,2)'))
    mfp.set_fem(gf.Fem('FEM_PK(3,0)'))

    mim = gf.MeshIm(m, gf.Integ('IM_TETRAHEDRON(5)'))

    topfaces = m.outer_faces_in_box([0.0,-0.01,0.011], [0.025, 0.08, 0.019])
    btmfaces = m.outer_faces_in_box([0.0,-0.01,-0.0061], [0.025, 0.08, -0.0059])
    NEUMANN_BOUNDARY = 1
    DIRICHLET_BOUNDARY = 2

    m.set_region(NEUMANN_BOUNDARY,   topfaces)
    m.set_region(DIRICHLET_BOUNDARY, btmfaces)

    md = gf.Model('real')
    md.add_fem_variable('u', mfu)
    md.add_initialized_data('cmu', Mu)
    md.add_initialized_data('clambda', Lambda)
    md.add_isotropic_linearized_elasticity_brick(mim, 'u', 'clambda', 'cmu')
    md.add_fem_variable('p', mfp)
    md.add_linear_incompressibility_brick(mim, 'u', 'p')
    md.add_initialized_data('VolumicData', [0,-1,0])
    md.add_source_term_brick(mim, 'u', 'VolumicData')

    # Attach the tripod to the ground
    md.add_Dirichlet_condition_with_multipliers(mim, 'u', mfu, 2)

    print('running solve...')
    md.solve('noisy', 'max iter', 1);
    U = md.variable('u');
    print('solve done!')
    
    sl.export_to_vtk(output_name, 'ascii', mfdu,  VM, 'Von Mises Stress', mfu, U, 'Displacement')
    
    print(f'Result is exported to {output_name}')
    
if __name__ == "__main__":
    mesh_name = sys.argv[1]
    output_name = sys.argv[2]
    
    main(mesh_name, output_name)
