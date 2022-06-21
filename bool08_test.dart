import 'package:test/test.dart';
import '../bin/bool08.dart';

void main() {
  test('bool08', () {
    expect(func(7), 7 % 1 == 0 && 7 >= 0);
  });
}
