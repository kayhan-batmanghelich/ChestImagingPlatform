ADD_TEST( NAME test_region_type_parser COMMAND nosetests ${CMAKE_CURRENT_BINARY_DIR}/test_region_type_parser.py )

ADD_TEST( NAME test_remap_lm COMMAND nosetests ${CMAKE_CURRENT_BINARY_DIR}/test_remap_lm.py )

ADD_TEST( NAME test_anonymize_dicom COMMAND nosetests ${CMAKE_CURRENT_BINARY_DIR}/test_anonymize_dicom.py )

ADD_TEST( NAME test_compute_dice_coefficient COMMAND nosetests ${CMAKE_CURRENT_BINARY_DIR}/test_compute_dice_coefficient.py )

ADD_TEST( NAME test_read_geometrytopologypoint_write_dataframe COMMAND nosetests ${CMAKE_CURRENT_BINARY_DIR}/test_read_geometrytopologypoint_write_dataframe.py )

