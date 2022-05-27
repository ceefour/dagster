const useFn = jest.fn(() => ({
  use: useFn,
  processSync: jest.fn((arg) => arg),
}));

export const remark = jest.fn(() => ({
  use: useFn,
}));
