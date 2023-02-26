import { render, screen } from '@testing-library/react';
import App from './App';

test('renders view dashboard link', () => {
  render(<App />);
  const linkElement = screen.getByText(/View Dashboard/i);
  expect(linkElement).toBeInTheDocument();
});
