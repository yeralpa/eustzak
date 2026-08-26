export const cap    = (s: string) => s.charAt(0).toUpperCase() + s.slice(1).toLowerCase();
export const person = (s: string) => s === 'NONE' ? '—' : s.toLowerCase();
