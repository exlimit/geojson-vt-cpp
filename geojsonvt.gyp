{
  'includes': [
    'deps/common.gypi',
    'deps/vars.gypi',
  ],
  'variables': {
    'gtest_static_libs%': '',
    'glfw_static_libs%': '',
  },
  'targets': [
    { 'target_name': 'geojsonvt',
      'product_name': 'geojsonvt',
      'type': 'static_library',
      'standalone_static_library': 1,

      'include_dirs': [
        'include',
      ],

      'sources': [
        'include/mapbox/geojsonvt/geojsonvt.hpp',
        'include/mapbox/geojsonvt/geojsonvt_tile.hpp',
        'include/mapbox/geojsonvt/geojsonvt_types.hpp',
        'src/geojsonvt.cpp',
        'src/geojsonvt_clip.cpp',
        'src/geojsonvt_clip.hpp',
        'src/geojsonvt_convert.cpp',
        'src/geojsonvt_convert.hpp',
        'src/geojsonvt_simplify.cpp',
        'src/geojsonvt_simplify.hpp',
        'src/geojsonvt_tile.cpp',
        'src/geojsonvt_util.hpp',
      ],

      'variables': {
        'cflags_cc': [
          '<@(variant_cflags)',
          '<@(rapidjson_cflags)',
        ],
        'ldflags': [],
        'libraries': [],
      },

      'conditions': [
        ['OS == "mac"', {
          'xcode_settings': {
            'OTHER_CPLUSPLUSFLAGS': [ '<@(cflags_cc)' ],
          },
        }, {
          'cflags_cc': [ '<@(cflags_cc)' ],
        }]
      ],

      'link_settings': {
        'conditions': [
          ['OS == "mac"', {
            'libraries': [ '<@(libraries)' ],
            'xcode_settings': { 'OTHER_LDFLAGS': [ '<@(ldflags)' ] }
          }, {
            'libraries': [ '<@(libraries)', '<@(ldflags)' ],
          }]
        ],
      },

      'direct_dependent_settings': {
        'include_dirs': [
          'include',
        ],
      },
    },

    { 'target_name': 'install',
      'type': 'none',
      'hard_dependency': 1,
      'dependencies': [
        'geojsonvt',
      ],

      'copies': [
        { 'files': [ '<(PRODUCT_DIR)/libgeojsonvt.a' ], 'destination': '<(install_prefix)/lib' },
        { 'files': [ '<!@(find include -name "*.hpp")' ], 'destination': '<(install_prefix)/include/mapbox/geojsonvt' },
      ],
    },
  ],

  'conditions': [
    ['gtest_static_libs != ""', {
      'targets': [
        { 'target_name': 'test',
          'product_name': 'test',
          'type': 'executable',

          'dependencies': [
            'geojsonvt',
          ],

          'include_dirs': [
            'src',
          ],

          'sources': [
            'test/test.cpp',
            'test/util.hpp',
            'test/util.cpp',
            'test/test_clip.cpp',
            'test/test_simplify.cpp',
          ],

          'variables': {
            'cflags_cc': [
              '<@(variant_cflags)',
              '<@(gtest_cflags)',
            ],
            'ldflags': [
              '<@(gtest_ldflags)'
            ],
            'libraries': [
              '<@(gtest_static_libs)',
            ],
          },

          'conditions': [
            ['OS == "mac"', {
              'libraries': [ '<@(libraries)' ],
              'xcode_settings': {
                'OTHER_CPLUSPLUSFLAGS': [ '<@(cflags_cc)' ],
                'OTHER_LDFLAGS': [ '<@(ldflags)' ],
              }
            }, {
              'cflags_cc': [ '<@(cflags_cc)' ],
              'libraries': [ '<@(libraries)', '<@(ldflags)' ],
            }]
          ],
        },
      ],
    }],
    ['glfw_static_libs != ""', {
      'targets': [
        { 'target_name': 'debug',
          'product_name': 'debug',
          'type': 'executable',

          'dependencies': [
            'geojsonvt',
          ],

          'include_dirs': [
            'src',
          ],

          'sources': [
            'debug/debug.cpp',
          ],

          'variables': {
            'cflags_cc': [
              '<@(variant_cflags)',
              '<@(glfw_cflags)',
            ],
            'ldflags': [
              '<@(glfw_ldflags)'
            ],
            'libraries': [
              '<@(glfw_static_libs)',
            ],
          },

          'conditions': [
            ['OS == "mac"', {
              'libraries': [ '<@(libraries)' ],
              'xcode_settings': {
                'OTHER_CPLUSPLUSFLAGS': [ '<@(cflags_cc)' ],
                'OTHER_LDFLAGS': [ '<@(ldflags)' ],
              }
            }, {
              'cflags_cc': [ '<@(cflags_cc)' ],
              'libraries': [ '<@(libraries)', '<@(ldflags)' ],
            }]
          ],
        },
      ],
    }],
  ],
}
