import 'package:test/test.dart';
import '../bin/bool06.dart';

void main() {
  test('bool06', () {
    expect(func(8), 8 % 2 == 0);
  });
}
