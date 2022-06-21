import 'package:test/test.dart';
import '../bin/bool05.dart';

void main() {
  test('bool05', () {
    expect(func(9), 9 % 2 == 1);
  });
}
