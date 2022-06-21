import 'package:test/test.dart';
import '../bin/bool09.dart';

void main() {
  test('bool09', () {
    expect(func(9), 9 % 1 == 0 && 9 > 0);
  });
}
