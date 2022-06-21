import 'package:test/test.dart';
import '../bin/bool03.dart';

void main() {
  test('bool03', () {
    expect(func(-8), -8 > 0);
  });
}
