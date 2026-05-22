describe('Meu primeiro teste - Pesquisa no Google', () => {

  it('Deve visitar o Google com sucesso', () => {
    cy.visit('https://www.google.com');
  });

  it('Deve fazer uma pesquisa no google', () => {
        cy.visit('https://www.google.com');
        cy.get('[name="q"]').type('Lorrany{enter}');
        cy.contains('Lorrany').should('be.visible');
    });
});
