#include "color.h"
#include "munit.h"

static MunitResult test_colors_defined(const MunitParameter params[], void* data) {
  (void) params;
  (void) data;

  munit_assert_int(RED, ==, 55);
  munit_assert_int(GREEN, ==, 176);
  munit_assert_int(BLUE, ==, 38);

  return MUNIT_OK;
}

static MunitResult test_colors_defined_correctly(const MunitParameter params[], void* data) {
  (void) params;
  (void) data;

  munit_assert_int(RED, !=, 0);
  munit_assert_int(GREEN, !=, 120);
  munit_assert_int(BLUE, !=, 215);

  return MUNIT_OK;
}

static MunitTest tests[] = {
  {
  "/are_defined",
  test_colors_defined,
  NULL,
  NULL,
  MUNIT_TEST_OPTION_NONE,
  NULL
  },
  {
  "/are_defined_correctly",
  test_colors_defined_correctly,
  NULL,
  NULL,
  MUNIT_TEST_OPTION_NONE,
  NULL
  },
  {
  NULL,
  NULL,
  NULL,
  NULL,
  MUNIT_TEST_OPTION_NONE,
  NULL
  }
};

static const MunitSuite suite = {
  "/colors",
  tests,
  NULL,
  1,
  MUNIT_SUITE_OPTION_NONE
};

int main(int argc, char* argv[MUNIT_ARRAY_PARAM(argc + 1)]) {
  return munit_suite_main(&suite, NULL, argc, argv);
}

// munit_case(RUN, test_color_enum1, {
//   assert_int(RED, ==, 0, "RED is defined as 0");
//   assert_int(GREEN, ==, 1, "GREEN is defined as 1");
//   assert_int(BLUE, ==, 2, "BLUE is defined as 2");
// });

// munit_case(SUBMIT, test_color_enum2, {
//   assert_int(RED, !=, 4, "RED is not defined as 4");
//   assert_int(GREEN, !=, 2, "GREEN is not defined as 2");
//   assert_int(BLUE, !=, 0, "BLUE is not defined as 0");
// });

// int main() {
//   MunitTest tests[] = {
//       munit_test("/are_defined", test_color_enum1),
//       munit_test("/are_defined_correctly", test_color_enum2),
//       munit_null_test,
//   };

//   MunitSuite suite = munit_suite("colors", tests);

//   return munit_suite_main(&suite, NULL, 0, NULL);
// }
