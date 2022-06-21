import 'package:test/test.dart';
import '../bin/bool04.dart';

void main() {
  test('bool04', () {
    expect(func(-8), -8 < 0);
  });
}
