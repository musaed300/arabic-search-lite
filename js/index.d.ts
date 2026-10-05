/** Remove Arabic diacritics and tatweel, unify alef, yaa, taa marbuta and waw-hamza forms, and lowercase. */
export declare function normalize(text: string | null | undefined): string;
export declare const version: string;
declare const lite: { normalize: typeof normalize; version: string };
export default lite;
